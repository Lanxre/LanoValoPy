from typing import List, Optional

from .henrik_api import HenrikAPI
from .game_api import GameApi
from .valo_types.valo_models import (
    AccountFetchByPUUIDOptionsModel,
    AccountFetchOptionsModel,
    GetContentFetchOptionsModel,
    GetCrosshairFetchOptionsModel,
    GetEsportsMatchesFetchOptionsModel,
    GetFeaturedItemsFetchOptionsModel,
    GetLeaderboardOptionsModel,
    GetLifetimeMMRHistoryFetchOptionsModel,
    GetMatchesByPUUIDFetchOptionsModel,
    GetMatchesFetchOptionsModel,
    GetMatchFetchOptionsModel,
    GetMMRByPUUIDFetchOptionsModel,
    GetMMRFetchOptionsModel,
    GetMMRHistoryByPUUIDFetchOptionsModel,
    GetMMRHistoryFetchOptionsModel,
    GetPremierTeamFetchOptionsModel,
    GetRawFetchOptionsModel,
    GetStatusFetchOptionsModel,
    GetStoreOffersFetchOptionsModel,
    GetVersionFetchOptionsModel,
    GetWebsiteFetchOptionsModel,
    GetPlayerCardModel,
    GetPlayerTitleModel,
    GetAgentsModel,
    GetGameMapsModel,
)
from .valo_types.valo_responses import (
    AccountResponseModelV1,
    AccountResponseModelV2,
    APIResponseModel,
    BinaryData,
    BuildGameInfoResponseModel,
    BundleResponseModelV2,
    CommunityNewsResponseModel,
    ContentResponseModel,
    EsportMatchDataResponseModel,
    FeaturedBundleResponseModelV1,
    LeaderboardDataResponseModelV2,
    LeaderboardDataResponseModelV3,
    MatchResponseModel,
    MMRHistoryByPuuidResponseModelV1,
    MMRResponseModel,
    PremierLeagueMatchesWrapperResponseModel,
    PremierTeamResponseModel,
    StatusDataResponseModel,
    StoreOffersResponseModelV1,
    StoreOffersResponseModelV2,
    PlayerTitleModelResponse,
    PlayerCardModelResponse,
    AgentResponseModel,
    MapModelResponse,
)

from .lanologger import LoggerBuilder

logger = LoggerBuilder("LanoValoPy").add_stream_handler().build()


class LanoValoPy:
    def __init__(
        self,
        henrik_token: Optional[str] = None,
        henrik_api: Optional[HenrikAPI] = None,
        game_api: Optional[GameApi] = None,
    ):
        self.henrik_api = henrik_api or HenrikAPI(henrik_token)
        self.game_api = game_api or GameApi()

        if henrik_token is None:
            logger.info(
                "Henrik token not provided. LanoValoPy will not be able to make some requests to the Henrik API."
            )

    @property
    def get_game_data(self) -> HenrikAPI:
        return self.henrik_api

    @property
    def get_game_api(self) -> GameApi:
        return self.game_api

    async def get_account(
        self, options: AccountFetchOptionsModel
    ) -> AccountResponseModelV1 | AccountResponseModelV2:
        """
        Gets the account information for a given name and tag.

        Args:
            options (AccountFetchOptionsModel): The options for the request.

        Returns:
            AccountResponseModelV1 | AccountResponseModelV2: The account information.
        """
        return await self.henrik_api.get_account(options)

    async def get_account_by_puuid(
        self, options: AccountFetchByPUUIDOptionsModel
    ) -> AccountResponseModelV1:
        """
        Gets the account information for a given puuid.

        Args:
            options (AccountFetchByPUUIDOptionsModel): The options for the request.

        Returns:
            AccountResponseModelV1: The account information.
        """
        return await self.henrik_api.get_account_by_puuid(options)

    async def get_mmr_by_puuid(
        self, options: GetMMRByPUUIDFetchOptionsModel
    ) -> MMRResponseModel:
        """
        Gets the MMR information for a given puuid.

        Args:
            options (GetMMRByPUUIDFetchOptionsModel): The options for the request.

        Returns:
            MMRResponseModel: The MMR information.
        """
        return await self.henrik_api.get_mmr_by_puuid(options)

    async def get_mmr_history_by_puuid(
        self, options: GetMMRHistoryByPUUIDFetchOptionsModel
    ) -> MMRHistoryByPuuidResponseModelV1:
        """
        Gets the MMR history for a given puuid.

        Args:
            options (GetMMRHistoryByPUUIDFetchOptionsModel): The options for the request.

        Returns:
            MMRHistoryByPuuidResponseModelV1: The MMR history.
        """
        return await self.henrik_api.get_mmr_history_by_puuid(options)

    async def get_matches_by_puuid(
        self, options: GetMatchesByPUUIDFetchOptionsModel
    ) -> List[MatchResponseModel]:
        return await self.henrik_api.get_matches_by_puuid(options)

    async def get_content(
        self, options: GetContentFetchOptionsModel
    ) -> ContentResponseModel:
        """
        Gets the content for the given locale. This endpoints returns basic contant data like season id's or skins.
        If you need more data, please refer to https://valorant-api.com which also has image data

        Args:
            options (GetContentFetchOptionsModel): The options for the request.

        Returns:
            ContentResponseModel: The content.
        """
        return await self.henrik_api.get_content(options)

    async def get_leaderboard(
        self, options: GetLeaderboardOptionsModel
    ) -> LeaderboardDataResponseModelV3 | LeaderboardDataResponseModelV2:
        """
        Gets the leaderboard for the given options.

        Args:
            options (GetLeaderboardOptionsModel): The options for the request.

        Returns:
            LeaderboardDataResponseModelV3 | LeaderboardDataResponseModelV2: The leaderboard data.
        """
        return await self.henrik_api.get_leaderboard(options)

    async def get_matches(
        self, options: GetMatchesFetchOptionsModel
    ) -> List[MatchResponseModel]:
        return await self.henrik_api.get_matches(options)

    async def get_match(self, options: GetMatchFetchOptionsModel) -> MatchResponseModel:
        """
        Gets the match data for the given match id.

        Args:
            options (GetMatchFetchOptionsModel): The options for the request.

        Returns:
            MatchResponseModel: The match data.
        """
        return await self.henrik_api.get_match(options)

    async def get_mmr_history(
        self, options: GetMMRHistoryFetchOptionsModel
    ) -> MMRResponseModel:
        """
        Returns the latest competitive games with RR movement for each game

        Args:
            options (GetMMRHistoryFetchOptionsModel): The options for the request.

        Returns:
            MMRResponseModel: The MMR history.
        """
        return await self.henrik_api.get_mmr_history(options)

    async def get_lifetime_mmr_history(
        self, options: GetLifetimeMMRHistoryFetchOptionsModel
    ) -> APIResponseModel:
        return await self.henrik_api.get_lifetime_mmr_history(options)

    async def get_mmr(self, options: GetMMRFetchOptionsModel) -> MMRResponseModel:
        """
        Gets the MMR information for a given name and tag.

        Args:
            options (GetMMRFetchOptionsModel): The options for the request.

        Returns:
            MMRResponseModel: The MMR information.
        """
        return await self.henrik_api.get_mmr(options)

    async def get_raw_data(self, options: GetRawFetchOptionsModel) -> APIResponseModel:
        """
        Make direct requests to the riot server and get the response without additional parsing from us

        Args:
            options (GetRawFetchOptionsModel): The options for the request.

        Returns:
            errors (APIResponseModel): The response from the server.
        """
        return await self.henrik_api.get_raw_data(options)

    async def get_status(
        self, options: GetStatusFetchOptionsModel
    ) -> StatusDataResponseModel:
        """
        Gets the status server for the given region.

        Args:
            options (GetStatusFetchOptionsModel): The options for the request.

        Returns:
            StatusDataResponseModel: The status server for the given region.
        """
        return await self.henrik_api.get_status(options)

    async def get_featured_items(
        self, options: GetFeaturedItemsFetchOptionsModel
    ) -> APIResponseModel | FeaturedBundleResponseModelV1 | List[BundleResponseModelV2]:
        return await self.henrik_api.get_featured_items(options)

    async def get_offers(
        self, options: GetStoreOffersFetchOptionsModel
    ) -> StoreOffersResponseModelV1 | StoreOffersResponseModelV2:
        """
        Gets the store offers.

        Args:
            options (GetStoreOffersFetchOptionsModel): The options for the request.

        Returns:
            StoreOffersResponseModelV1: The store offers.

        Raises:
            ValueError: If the version is invalid.
        """
        return await self.henrik_api.get_offers(options)

    async def get_version(
        self, options: GetVersionFetchOptionsModel
    ) -> BuildGameInfoResponseModel:
        """
        Gets the current build version and branch for a given region.

        Args:
            options (GetVersionFetchOptionsModel): The options for the request.

        Returns:
            BuildGameInfoResponseModel: The current build version and branch.
        """
        return await self.henrik_api.get_version(options)

    async def get_website(
        self, options: GetWebsiteFetchOptionsModel
    ) -> List[CommunityNewsResponseModel]:
        """
        Gets the community news for a given country code and filter.

        Args:
            options (GetWebsiteFetchOptionsModel): The options for the request.

        Returns:
            List[CommunityNewsResponseModel]: The community news.
        """
        return await self.henrik_api.get_website(options)

    async def get_crosshair(self, options: GetCrosshairFetchOptionsModel) -> BinaryData:
        """
        Gets a crosshair image as a binary response.

        Args:
            options (GetCrosshairFetchOptionsModel): The options for the request.

        Returns:
            BinaryData: The binary response from the server. This binary response is a PNG image.
        """
        return await self.henrik_api.get_crosshair(options)

    async def get_esports_matches(
        self, options: GetEsportsMatchesFetchOptionsModel
    ) -> List[EsportMatchDataResponseModel]:
        """
        Gets the current esports matches.

        Returns:
            List[EsportsMatchResponseModel]: The current esports matches.
        """
        return self.henrik_api.get_esports_matches(options)

    async def get_premier_team(
        self, options: GetPremierTeamFetchOptionsModel
    ) -> PremierTeamResponseModel:
        """
        Gets the premier team.

        Args:
            options (GetPremierTeamFetchOptionsModel): The options for the request.

        Returns:
            PremierTeamResponseModel: The premier team.
        """
        return await self.henrik_api.get_premier_team(options)

    async def get_premier_team_history(
        self, options: GetPremierTeamFetchOptionsModel
    ) -> PremierLeagueMatchesWrapperResponseModel:
        """
        Gets the premier team history.

        Args:
            options (GetPremierTeamFetchOptionsModel): The options for the request.

        Returns:
            PremierLeagueMatchesWrapperResponseModel: The premier team history.
        """
        return await self.henrik_api.get_premier_team_history(options)

    async def get_premier_team_by_id(self, team_id: str) -> PremierTeamResponseModel:
        """
        Gets the premier team.

        Args:
            options (GetPremierTeamFetchOptionsModel): The options for the request.

        Returns:
            PremierTeamResponseModel: The premier team.
        """
        return await self.henrik_api.get_premier_team_by_id(team_id)

    async def get_premier_team_history_by_id(
        self, team_id: str
    ) -> PremierLeagueMatchesWrapperResponseModel:
        """
        Gets the premier team history.

        Args:
            options (GetPremierTeamFetchOptionsModel): The options for the request.

        Returns:
            PremierLeagueMatchesWrapperResponseModel: The premier team history.
        """
        return await self.henrik_api.get_premier_team_history_by_id(team_id)

    async def get_player_cards(
        self, options: GetPlayerCardModel
    ) -> List[PlayerCardModelResponse]:
        return await self.game_api.get_player_cards(options)

    async def get_player_card_by_uuid(
        self, options: GetPlayerCardModel
    ) -> PlayerCardModelResponse:
        return await self.game_api.get_player_card_by_uuid(options)

    async def get_player_titles(
        self, options: GetPlayerTitleModel
    ) -> List[PlayerTitleModelResponse]:
        """
        Gets the player titles.

        Args:
            options (GetPlayerTitleModel): The options for the request.

        Returns:
            List[PlayerTitleModelResponse]: The player titles.
        """
        return await self.game_api.get_player_titles(options)

    async def get_player_title_by_uuid(
        self, options: GetPlayerTitleModel
    ) -> PlayerTitleModelResponse:
        """
        Fetches a player title by UUID.

        Args:
            options (GetPlayerTitleModel): The options containing the UUID of the player title
            and optional language preference.

        Returns:
            PlayerTitleModelResponse: The response model containing details of the player title.

        Raises:
            ValidationError: If the UUID is not provided in the options.
        """
        return await self.game_api.get_player_title_by_uuid(options)

    async def get_agents(self, options: GetAgentsModel) -> List[AgentResponseModel]:
        return await self.game_api.get_agents(options)

    async def get_agent_by_uuid(self, options: GetAgentsModel) -> AgentResponseModel:
        return await self.game_api.get_agent_by_uuid(options)

    async def get_maps(self, options: GetGameMapsModel) -> List[MapModelResponse]:
        return await self.game_api.get_maps(options)

    async def get_map_by_uuid(self, options: GetGameMapsModel) -> MapModelResponse:
        return await self.game_api.get_map_by_uuid(options)