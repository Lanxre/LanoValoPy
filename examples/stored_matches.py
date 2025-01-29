import os
import sys

from lano_valo_py.valo_types.valo_enums import Regions
from lano_valo_py.valo_types.valo_models import (
    GetStoredMatchesFilterModel,
    GetStoredMatchesOptionsModel,
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy


async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    option_filter = GetStoredMatchesFilterModel(
        size=20
    )

    match_options = GetStoredMatchesOptionsModel(
        region=Regions.eu,
        name="Lanore",
        tag="evil",
        filter=option_filter,
    )
    stored_match_response = await api_client.get_stored_matches(match_options)
    print(stored_match_response)


if __name__ == "__main__":
    asyncio.run(main())
