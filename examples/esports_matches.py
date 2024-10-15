import sys
import os

from lano_valo_py.valo_types.valo_enums import EsportsRegions, EsportsLeagues
from lano_valo_py.valo_types.valo_models import GetEsportsMatchesFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(token="YOUR_TOKEN_HERE")

    # Example: Get Game Content
    options = GetEsportsMatchesFetchOptionsModel(region=EsportsRegions.international)
    response = await api_client.get_esports_matches(options)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
