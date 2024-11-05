import pytest
from lano_valo_py import LanoValoPy
from lano_valo_py.valo_types.valo_enums import Locales
from lano_valo_py.valo_types.valo_models import GetPlayerCardModel, GetPlayerTitleModel


@pytest.fixture(scope="module")
def game_content():
    return LanoValoPy().game_api


@pytest.mark.asyncio
async def test_get_player_cards(game_content):
    options = GetPlayerCardModel(language=Locales.ru_RU)
    player_cards = await game_content.get_player_cards(options)
    assert len(player_cards) > 0


@pytest.mark.asyncio
async def test_get_player_card_by_uuid(game_content):
    options = GetPlayerCardModel(
        language=Locales.ru_RU, uuid="33c1f011-4eca-068c-9751-f68c788b2eee"
    )
    player_card = await game_content.get_player_card_by_uuid(options)
    assert player_card


@pytest.mark.asyncio
async def test_get_player_titles(game_content):
    options = GetPlayerTitleModel(language=Locales.ru_RU)
    player_titles = await game_content.get_player_titles(options)
    assert len(player_titles) > 0


@pytest.mark.asyncio
async def test_get_player_title_by_uuid(game_content):
    options = GetPlayerTitleModel(
        language=Locales.ru_RU, uuid="48d870a2-4493-ebf8-7d6f-979be914dc43"
    )
    player_title = await game_content.get_player_title_by_uuid(options)
    assert player_title


@pytest.mark.asyncio
async def test_get_maps(game_content):
    options = GetPlayerTitleModel(language=Locales.ru_RU)
    maps = await game_content.get_maps(options)
    assert len(maps) > 0


@pytest.mark.asyncio
async def test_get_map_by_uuid(game_content):
    options = GetPlayerTitleModel(
        language=Locales.ru_RU, uuid="7eaecc1b-4337-bbf6-6ab9-04b8f06b3319"
    )
    map = await game_content.get_map_by_uuid(options)
    assert map
