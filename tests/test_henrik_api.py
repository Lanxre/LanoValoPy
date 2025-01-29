import pytest

from lano_valo_py import LanoValoPy
from lano_valo_py.valo_types.valo_enums import CCRegions, MMRVersions, Regions, Maps, Modes
from lano_valo_py.valo_types.valo_models import GetWebsiteFetchOptionsModel, GetMMRByPUUIDFetchOptionsModel, GetStoredMatchesOptionsModel, GetStoredMatchesFilterModel

from tests import Settings

@pytest.fixture(scope="module")
def get_lanovalopy():
    settings = Settings()
    return LanoValoPy(settings.henrik_api_token)


@pytest.mark.asyncio
async def test_get_valorant_news(get_lanovalopy: LanoValoPy):
    website_options = GetWebsiteFetchOptionsModel(country_code=CCRegions.ru_ru)
    website_response = await get_lanovalopy.get_website(website_options)
    assert len(website_response) > 0


@pytest.mark.asyncio
async def test_get_mmr_by_puuid(get_lanovalopy: LanoValoPy):
    mmr_options = GetMMRByPUUIDFetchOptionsModel(
        version=MMRVersions.v2,
        region=Regions.eu,
        puuid='e4122af3-fa8c-582c-847d-42a3868925cd',
    )
    mmr_response = await get_lanovalopy.get_mmr_by_puuid(mmr_options)
    assert mmr_response.current_data.elo

@pytest.mark.asyncio
async def test_get_stored_matches(get_lanovalopy: LanoValoPy):
    stored_matches_options = GetStoredMatchesOptionsModel(
        region=Regions.eu,
        name="Lanore",
        tag="evil",
        map=Maps.bind,
        mode=Modes.competitive,
        filter = GetStoredMatchesFilterModel(size=20)
    )
    stored_matches_response = await get_lanovalopy.get_stored_matches(stored_matches_options)
    assert len(stored_matches_response)