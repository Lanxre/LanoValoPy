import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from lano_valo_py.valo_types.valo_enums import Regions
from lano_valo_py.valo_types.valo_models import GetStatusFetchOptionsModel

import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(token="YOUR_TOKEN_HERE")
    
    # Example: Get Server Status
    store_options = GetStatusFetchOptionsModel(region=Regions.eu)
    store_items = await api_client.get_status(store_options)
    print(store_items)


if __name__ == "__main__":
    asyncio.run(main())
