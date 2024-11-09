import sys
import os

from lano_valo_py.valo_types.valo_enums import Regions
from lano_valo_py.valo_types.valo_models import GetLifetimeMMRHistoryFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get MMR Lifetime History
    mmr_options = GetLifetimeMMRHistoryFetchOptionsModel(region=Regions.eu, name="Lanore", tag="evil")
    mmr_response = await api_client.get_lifetime_mmr_history(mmr_options)
    print(mmr_response)


if __name__ == "__main__":
    asyncio.run(main())
