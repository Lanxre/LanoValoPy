import sys
import os

from lano_valo_py.valo_types.valo_enums import MMRVersions, Regions, AccountVersion
from lano_valo_py.valo_types.valo_models import GetMMRHistoryByPUUIDFetchOptionsModel, AccountFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    api_client = LanoValoPy(henrik_token="HDEV-d9b7fa0f-adcf-4367-a92a-0625f964ab49")

    account = await api_client.get_account(
        AccountFetchOptionsModel(name="fofifkifirom", tag="arbuz",version=AccountVersion.v2))

    options = GetMMRHistoryByPUUIDFetchOptionsModel(
        version=MMRVersions.v2,
        region=Regions.eu,
        puuid= account.puuid,
    )
    data = await api_client.get_player_day_wins_loses_stats(options=options)
    print(data) # if no daily stats, will return None


if __name__ == "__main__":
    asyncio.run(main())
