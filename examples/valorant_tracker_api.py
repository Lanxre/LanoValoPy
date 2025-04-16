import sys
import os

from lano_valo_py.valo_tracker.tracker_options import TrackerAccountOptions

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    client = LanoValoPy()

    user_options = TrackerAccountOptions(username="Lanore", tag="evil")
    user_data = await client.tracker_api.get_user_data(user_options)
    
    # user of data
    print(user_data)



if __name__ == "__main__":
    asyncio.run(main())
