import sys
import os

from lano_valo_py.valo_types.valo_models import GetMatchFetchOptionsModel, AccountFetchOptionsModelV2

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")
    player_options = AccountFetchOptionsModelV2(name="LANORE", tag="evil")
    # or player_options = AccountFetchOptionsModelV2(puuid="e4122af3-fa8c-582c-847d-42a3868925cd")
    match_options = GetMatchFetchOptionsModel(match_id="e2ca5f5f-70f4-49a3-b77e-2389dca5e3b4")
    player_match_stats = await api_client.get_player_match_stats(player_options, match_options)
    print(player_match_stats)

if __name__ == "__main__":
    asyncio.run(main())
