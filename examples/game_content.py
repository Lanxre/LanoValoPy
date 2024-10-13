import sys
import os

from lano_valo_py.valo_types.valo_enums import Locales
from lano_valo_py.valo_types.valo_models import GetContentFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(token="YOUR_TOKEN_HERE")

    # Example: Get Game Content
    game_content_options = GetContentFetchOptionsModel(locale=Locales.ru_RU)
    game_content_response = await api_client.get_content(game_content_options)
    print(game_content_response)


if __name__ == "__main__":
    asyncio.run(main())
