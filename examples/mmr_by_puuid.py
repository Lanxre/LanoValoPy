import sys
import os

from lano_valo_py.valo_types.valo_enums import MMRVersions, Regions
from lano_valo_py.valo_types.valo_models import GetMMRByPUUIDFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get MMR by PUUID
    mmr_options = GetMMRByPUUIDFetchOptionsModel(
        version=MMRVersions.v2,
        region=Regions.eu,
        puuid='e4122af3-fa8c-582c-847d-42a3868925cd',
    )
    mmr_response = await api_client.get_mmr_by_puuid(mmr_options)
    print(mmr_response)


if __name__ == "__main__":
    asyncio.run(main())
