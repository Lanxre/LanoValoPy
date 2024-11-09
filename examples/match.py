import sys
import os

from lano_valo_py.valo_types.valo_models import GetMatchFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get Match
    options = GetMatchFetchOptionsModel(match_id="696848f3-f16f-45bf-af13-e2192f81a600")
    response = await api_client.get_match(options)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
