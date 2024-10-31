import sys
import os

from lano_valo_py.valo_types.valo_enums import Locales
from lano_valo_py.valo_types.valo_models import GetPlayerCardModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    api_client = LanoValoPy()

    # Example: Get All Players Card
    options = GetPlayerCardModel(language=Locales.ru_RU)
    player_cards = await api_client.get_player_cards(options)
    print(player_cards)

    # Example: Get Player Card By PUUID
    card_uuid = "33c1f011-4eca-068c-9751-f68c788b2eee"
    options = GetPlayerCardModel(language=Locales.ru_RU, uuid=card_uuid)
    player_card = await api_client.get_player_card_by_uuid(options)
    print(player_card)


if __name__ == "__main__":
    asyncio.run(main())
