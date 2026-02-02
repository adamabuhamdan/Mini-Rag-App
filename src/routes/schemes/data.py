from pydantic import BaseModel
from typing import Optional


class ProssesRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100
    overlap_size: Optional[int] = 20
    reset: Optional[int] = 0