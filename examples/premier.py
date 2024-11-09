import sys
import os

from lano_valo_py.valo_types.valo_models import GetPremierTeamFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get Premier Team
    options = GetPremierTeamFetchOptionsModel(team_name="YARI Esports", team_tag="YARI")
    response = await api_client.get_premier_team(options)
    print(response)

    # Example: Get Premier Team History
    options = GetPremierTeamFetchOptionsModel(team_name="YARI Esports", team_tag="YARI")
    response = await api_client.get_premier_team_history(options)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
