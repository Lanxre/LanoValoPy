import sys
import os

from lano_valo_py.valo_types.valo_enums import Regions, LeaderboardVersions
from lano_valo_py.valo_types.valo_models import GetLeaderboardOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(token="YOUR_TOKEN_HERE")

    # Example: Get Leaderboard
    options = GetLeaderboardOptionsModel(region=Regions.eu, version=LeaderboardVersions.v3)
    response = await api_client.get_leaderboard(options)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
