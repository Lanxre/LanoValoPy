import cloudscraper
from pydantic import ValidationError

from ..based_api import BasedApi
from ..lanologger import LoggerBuilder
from ..utils.const import VALIDATE_DATA_MESSAGE_ERROR
from ..utils.tools import convert_model
from .tracker_options import TrackerAccountOptions
from .tracker_response import (
    Segment,
    SegmentSeasonStats,
    TrackerResponse,
    TrackerUserData,
)

logger = LoggerBuilder("TrackerApi").add_stream_handler().build()


class TrackerApi(BasedApi):
    base_url = "https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}"
    segment_url = "https://api.tracker.gg/api/v2/valorant/standard/profile/riot/{username}%23{tag}/segments/season?playlist={playlist}&seasonId={season_id}&source=web"

    def __init__(self):
        super().__init__()
        self._cloudscraper = cloudscraper.create_scraper(
            browser={
                "browser": "firefox",
                "platform": "linux",
                "desktop": True,
                "mobile": False,
            }
        )

    async def get_account(self, options: TrackerAccountOptions) -> TrackerResponse:
        try:
            tracker_response = self._cloudscraper.get(
                self.base_url.format(username=options.username, tag=options.tag)
            )
            if not tracker_response.text or tracker_response.text.startswith("<!doctypehtml>"):
                logger.error(f"{VALIDATE_DATA_MESSAGE_ERROR} Data: {tracker_response.text}")
                raise ValueError("Some wrong")
            
            tracker_data = TrackerResponse.model_validate_json(tracker_response.text)

            season_id = (
                tracker_data.data.metadata.seasons[0].id
                or tracker_data.data.metadata.defaultSeason
            )
            playlists = tracker_data.data.metadata.playlists

            for plalist in playlists:
                segment_responce = self._cloudscraper.get(
                    self.segment_url.format(
                        username=options.username,
                        tag=options.tag,
                        playlist=plalist.id,
                        season_id=season_id,
                    )
                )

                if segment_responce.text:
                    segment_data = Segment.model_validate_json(tracker_response.text)
                    tracker_data.data.segments.append(segment_data)

            return tracker_data

        except ValidationError as e:
            raise ValueError(f"{VALIDATE_DATA_MESSAGE_ERROR}: {e}") from e

    async def get_user_data(self, options: TrackerAccountOptions) -> TrackerUserData:
        account = await self.get_account(options)
        logger.warning(f"ACOUNT DATA: {account.data}")
        try:
            segment_data = list(
                filter(
                    lambda x: x.attributes.playlist == "competitive",
                    account.data.segments,
                )
            )[0]
            logger.warning(f"FILTERED DATA {segment_data}")
            segment_data = convert_model(
                source=Segment,
                target_model=SegmentSeasonStats,
            )
            return TrackerUserData(
                uuid=account.data.platformInfo.platformUserId,
                platform=account.data.platformInfo.platformSlug,
                name=account.data.platformInfo.platformUserHandle,
                userid=account.data.platformInfo.platformUserIdentifier,
                avatar=account.data.platformInfo.avatarUrl,
                pageViews=account.data.userInfo.pageviews,
                rank=segment_data.rank.metadata.tierName,
                peakRank=segment_data.peakRank.metadata.tierName,
            )
        except Exception as e:
            ValueError(f"{VALIDATE_DATA_MESSAGE_ERROR}: {e}")

    async def get_all_gamemodes(self): ...

    async def get_ranked(self): ...

    async def get_unrated(self): ...

    async def get_agents(self, options: TrackerAccountOptions):
        res = await self.get_account(options)
        try:
            agents = list(
                filter(
                    lambda x: x.type == "agent",
                    res.data.segments,
                )
            )
            
        except Exception as e:
            ValueError(f"{VALIDATE_DATA_MESSAGE_ERROR}: {e}")