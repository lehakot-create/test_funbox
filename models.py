from pydantic import BaseModel
from typing import List


class Links(BaseModel):
    links: List[str]
