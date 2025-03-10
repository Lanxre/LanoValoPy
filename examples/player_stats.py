import sys
import os

from lano_valo_py.valo_types.valo_enums import MMRVersions, Regions, AccountVersion
from lano_valo_py.valo_types.valo_models import GetMMRHistoryByPUUIDFetchOptionsModel, AccountFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    account = await api_client.get_account(
        AccountFetchOptionsModel(name="Lanore", tag="evil",version=AccountVersion.v2))

    options = GetMMRHistoryByPUUIDFetchOptionsModel(
        version=MMRVersions.v2,
        region=Regions.eu,
        puuid= account.puuid,
    )
    data = await api_client.get_player_day_wins_loses_stats(options=options)
    print(data) # if no daily stats, will return None


if __name__ == "__main__":
    asyncio.run(main())
