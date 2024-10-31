import sys
import os

from lano_valo_py.valo_types.valo_enums import Locales
from lano_valo_py.valo_types.valo_models import GetPlayerTitleModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    api_client = LanoValoPy()

    # Example: Get All Players Card
    options = GetPlayerTitleModel(language=Locales.ru_RU)
    player_titles = await api_client.get_player_cards(options)
    print(player_titles)

    # Example: Get Player Card By PUUID
    title_uuid = "48d870a2-4493-ebf8-7d6f-979be914dc43"
    options = GetPlayerTitleModel(language=Locales.ru_RU, uuid=title_uuid)
    player_title= await api_client.get_player_title_by_uuid(options)
    print(player_title)


if __name__ == "__main__":
    asyncio.run(main())
