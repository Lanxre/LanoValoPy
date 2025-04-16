from pydantic import BaseModel

class TrackerAccountOptions(BaseModel):
    username: str
    tag: str
    