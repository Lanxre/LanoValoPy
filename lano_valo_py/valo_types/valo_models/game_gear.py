from typing import Optional

from pydantic import BaseModel

from ..valo_enums import Locales


class GetGameGearModel(BaseModel):
    uuid: Optional[str] = None
    language: Optional[Locales] = Locales.en_US
