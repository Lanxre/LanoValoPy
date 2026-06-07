<div align="center">

[![Downloads](https://static.pepy.tech/badge/lanovalopy)](https://pepy.tech/project/lanovalopy)

</div>

# LanoValoPy (Lanore Valorant Python)

LanoValoPy is a python-based wrapper for the following Valorant Rest API

[ORIGINAL API](https://github.com/Henrik-3/unofficial-valorant-api)

### API KEY

You can get API KEY on [Henrik's discord server](https://discord.com/invite/X3GaVkX2YN) or [Henrik's dashboard](https://api.henrikdev.xyz/dashboard/)

[OPENAPI SPEC](https://api.henrikdev.xyz/docs)
[DOCS](https://status.henrikdev.xyz)

## Download

``` bash
pip install lanovalopy@latest
```

## EXAMPLES

[For more examples](./examples/)

### Get Account

```python
import asyncio
from lano_valo_py import LanoValoPy
from lano_valo_py.valo_types.valo_enums import MMRVersions, Regions

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get Account Information
    account_options = AccountFetchOptionsModel(name="LANORE", tag="evil")
    try:
        account_response = await api_client.get_account(account_options)
        print(account_response)
    except Exception as e:
        print(f"Error fetching account: {e}")

if __name__ == "__main__":
    asyncio.run(main())

```

### Get Stored-MMR-History 
```python

from lano_valo_py.valo_types.valo_enums import MMRVersions, Regions
from lano_valo_py.valo_types.valo_models import (
    GetMMRStoredHistoryFilterModel,
    GetMMRStoredHistoryOptionsModel,
    GetMMRStoredHistoryByPUUIDResponseModel
)

import asyncio

from lano_valo_py import LanoValoPy


async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="You_token_here")

    # Example: Get Stored MMR History

    # Use filter if u have more than 20 match in one episode
    option_filter = GetMMRStoredHistoryFilterModel(
        size=20
    )  # max size one one page is 20, page is 1 by default

    mmr_options = GetMMRStoredHistoryOptionsModel(
        version=MMRVersions.v1,
        region=Regions.eu,
        name="Lanore",
        tag="evil",
        filter=option_filter,
    )
    stored_mmr_history_response = await api_client.get_stored_mmr_history(mmr_options)
    print(stored_mmr_history_response)

    # Example: Get Stored MMR History By PUUID
    mmr_options = GetMMRStoredHistoryByPUUIDResponseModel(
        version=MMRVersions.v1,
        region=Regions.eu,
        puuid="e4122af3-fa8c-582c-847d-42a3868925cd",
        filter=option_filter,
    )
    stored_mmr_history_response = await api_client.get_stored_mmr_history_by_puuid(mmr_options)
    print(stored_mmr_history_response)

```

## Supported Endpoints
- Account info
- MMR history
- Match history
- Stored Data
- etc...

## Rate Limits
The unofficial Valorant API has the following limits:
- Basic key: 30 requests per minute
- Advanced key: 90 requests per minute
- Custom key: Limit you requests

### Common Use Cases
- Track player rank over time
- Compare teammates' stats
- Monitor store rotations