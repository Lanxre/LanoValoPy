import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lano_valo_py.valo_types.valo_enums import FeaturedItemsVersion
from lano_valo_py.valo_types.valo_models import GetStoreOffersFetchOptionsModel

import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")
    
    # Example: Get Offers v1 | v2
    offers_options = GetStoreOffersFetchOptionsModel(version=FeaturedItemsVersion.v2)
    offers = await api_client.get_offers(offers_options)
    print(offers)


if __name__ == "__main__":
    asyncio.run(main())
