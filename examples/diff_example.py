import os
import sys

from examples.config import Settings
from lano_valo_py.valo_types.valo_enums.general import Modes
from lano_valo_py.valo_types.valo_enums.regions import Regions
from lano_valo_py.valo_types.valo_enums.versions import MatchListVersion
from lano_valo_py.valo_types.valo_models.match import GetMatchesFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    # Get token from .env
    settings = Settings()

    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token=settings.henrik_api_token)
    options = GetMatchesFetchOptionsModel(
        name="Lanore",
        tag="evil",
        region=Regions.eu,
        version=MatchListVersion.v4,
        filter=Modes.competitive,
        size=10,
    )

    most_played_with = await api_client.get_most_played(options, 10)
    print(most_played_with)


if __name__ == "__main__":
    asyncio.run(main())
