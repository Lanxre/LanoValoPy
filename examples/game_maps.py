import sys
import os

from lano_valo_py.valo_types.valo_enums import Locales
from lano_valo_py.valo_types.valo_models import GetGameMapsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    api_client = LanoValoPy()

    # Example: Get All Game Maps
    options = GetGameMapsModel(language=Locales.ru_RU)
    maps = await api_client.get_maps(options)
    print(maps)

    # Example: Get Game Map By PUUID
    map_uuid = "7eaecc1b-4337-bbf6-6ab9-04b8f06b3319"
    options = GetGameMapsModel(language=Locales.ru_RU, uuid=map_uuid)
    map = await api_client.get_map_by_uuid(options)
    print(map)


if __name__ == "__main__":
    asyncio.run(main())
