import sys
import os

from lano_valo_py.valo_types.valo_enums import Locales
from lano_valo_py.valo_types.valo_models import GetAgentsModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import asyncio

from lano_valo_py import LanoValoPy

async def main():
    api_client = LanoValoPy()

    # Example: Get All Agents Card
    options = GetAgentsModel(language=Locales.ru_RU)
    agents = await api_client.get_agents(options)
    print(agents)

    # Example: Get Agent Card By PUUID
    title_uuid = "ded3520f-4264-bfed-162d-b080e2abccf9" # Sova
    options = GetAgentsModel(language=Locales.ru_RU, uuid=title_uuid)
    agent = await api_client.get_agent_by_uuid(options)
    print(agent)


if __name__ == "__main__":
    asyncio.run(main())
