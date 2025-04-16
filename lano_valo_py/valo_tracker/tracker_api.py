from pydantic import ValidationError

from ..based_api import BasedApi
from ..lanologger import LoggerBuilder
from ..utils.const import VALIDATE_DATA_MESSAGE_ERROR
from ..utils.tools import convert_model
from ..valo_types.valo_models import FetchOptionsModel
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

    async def get_account(self, options: TrackerAccountOptions) -> TrackerResponse:
        fetch_options = FetchOptionsModel(
            url=self.base_url.format(username=options.username, tag=options.tag)
        )
        tracker_response = await self._fetch(fetch_options)
        try:

            if not tracker_response.data:
                return None

            tracker_data = TrackerResponse.model_validate(tracker_response.data)

            season_id = (
                tracker_data.data.metadata.seasons[0].id
                or tracker_data.data.metadata.defaultSeason
            )
            playlists = tracker_data.data.metadata.playlists

            for plalist in playlists:
                segment_responce = await self._fetch(
                    FetchOptionsModel(
                        url=self.segment_url.format(
                            username=options.username,
                            tag=options.tag,
                            plalist=plalist.id,
                            season_id=season_id,
                        )
                    )
                )

                if not segment_responce.data:
                    segment_data = Segment.model_validate(segment_responce.data)
                    tracker_data.data.segments.append(segment_data)

            return tracker_data

        except ValidationError as e:
            raise ValueError(f"{VALIDATE_DATA_MESSAGE_ERROR}: {e}") from e

    async def get_user_data(self, options: TrackerAccountOptions) -> TrackerUserData:
        account = await self.get_account(options)
        try:
            segment_data = list(
                filter(
                    lambda x: x.attributes.playlist == "competitive",
                    account.data.segments,
                )
            )[0]
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
