from pydantic import BaseModel
from typing import List


class LogoIcon(BaseModel):
    name: str
    src: str
    url: str


LogoIconList = List[LogoIcon]
