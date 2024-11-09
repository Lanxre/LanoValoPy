import sys
import os

from lano_valo_py.valo_types.valo_enums import CCRegions
from lano_valo_py.valo_types.valo_models import GetWebsiteFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get VALORANT news
    website_options = GetWebsiteFetchOptionsModel(country_code=CCRegions.ru_ru)
    website_response = await api_client.get_website(website_options)
    print(website_response)


if __name__ == "__main__":
    asyncio.run(main())
