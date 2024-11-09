import os
import sys

from lano_valo_py.valo_types.valo_enums import MMRVersions, Regions
from lano_valo_py.valo_types.valo_models import (
    GetMMRStoredHistoryFilterModel,
    GetMMRStoredHistoryOptionsModel,
    GetMMRStoredHistoryByPUUIDResponseModel
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get Stored MMR History

    # Use filter if u have more than 20 match in one episode
    option_filter = GetMMRStoredHistoryFilterModel(
        size=20
    )  # max size one one page is 20, page is 1 by default

    mmr_options = GetMMRStoredHistoryOptionsModel(
        version=MMRVersions.v1,
        region=Regions.eu,
        name="Lanore",
        tag="evil",
        filter=option_filter,
    )
    stored_mmr_history_response = await api_client.get_stored_mmr_history(mmr_options)
    print(stored_mmr_history_response)

    # Example: Get Stored MMR History By PUUID
    mmr_options = GetMMRStoredHistoryByPUUIDResponseModel(
        version=MMRVersions.v1,
        region=Regions.eu,
        puuid="e4122af3-fa8c-582c-847d-42a3868925cd",
        filter=option_filter,
    )
    stored_mmr_history_response = await api_client.get_stored_mmr_history_by_puuid(mmr_options)
    print(stored_mmr_history_response)


if __name__ == "__main__":
    asyncio.run(main())
