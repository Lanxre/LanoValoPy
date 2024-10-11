import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    api = LanoValoPy(token="YOUR_TOKEN_HERE")

    # Get account details
    account_data = await api.get_account(name="LANORE", tag="evil")
    if account_data.error:
        print(f"Error {account_data.status}: {account_data.error}")
    else:
        print(f"Account Data: {account_data.data}")

    # Get MMR
    mmr_data = await api.get_mmr(version="v1", region="eu", name="LANORE", tag="evil")
    if mmr_data.error:
        print(f"Error {mmr_data.status}: {mmr_data.error}")
    else:
        print(f"MMR Data: {mmr_data.data}")


if __name__ == "__main__":
    asyncio.run(main())
