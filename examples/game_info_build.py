import sys
import os

from lano_valo_py.valo_types.valo_enums import Regions
from lano_valo_py.valo_types.valo_models import GetVersionFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(token="YOUR_TOKEN_HERE")

    # Example: Get Game Information
    game_options = GetVersionFetchOptionsModel(region=Regions.eu)
    game_response = await api_client.get_version(game_options)
    print(game_response)


if __name__ == "__main__":
    asyncio.run(main())
