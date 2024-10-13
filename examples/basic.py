import sys
import os

from lano_valo_py.valo_types.valo_enums import MMRVersions, Regions
from lano_valo_py.valo_types.valo_models import AccountFetchOptionsModel, GetMMRFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(token="YOUR_TOKEN_HERE")

    # Example: Get Account Information
    account_options = AccountFetchOptionsModel(name="LANORE", tag="evil")
    account_response = await api_client.get_account(account_options)
    print(account_response)

    # Example: Get MMR by PUUID
    mmr_options = GetMMRFetchOptionsModel(
        version=MMRVersions.v1,
        region=Regions.eu,
        name="Lanore",
        tag="evil",
    )
    mmr_response = await api_client.get_mmr(mmr_options)
    print(mmr_response)


if __name__ == "__main__":
    asyncio.run(main())
