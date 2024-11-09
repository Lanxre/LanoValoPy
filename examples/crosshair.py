import sys
import os


from lano_valo_py.valo_types.valo_models import GetCrosshairFetchOptionsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    # Initialize the API client with your token
    api_client = LanoValoPy(henrik_token="YOUR_TOKEN_HERE")

    # Example: Get Crosshair | You also can input size
    croshair_code="0;P;c;5;t;3;o;1;f;0;m;1;0t;4;0l;5;0o;0;0a;1;0f;0;1t;8;1l;3;1o;0;1a;1;1m;0;1f;0"
    crosshair_options = GetCrosshairFetchOptionsModel(code=croshair_code)
    crosshair_response = await api_client.get_crosshair(crosshair_options)
    with open("crosshair.png", "wb") as f:
        f.write(crosshair_response)


if __name__ == "__main__":
    asyncio.run(main())
