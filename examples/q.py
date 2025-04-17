import sys
import os

from lano_valo_py.valo_tracker.tracker_options import TrackerAccountOptions

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    client = LanoValoPy()
    options = TrackerAccountOptions(username="Lanore", tag="evil") 

    # user info
    user_info = await client.tracker_api.get_user_data(options)
    print(user_info)



if __name__ == "__main__":
    asyncio.run(main())
