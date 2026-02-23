from pydantic import BaseModel, Field
from typing import List


class SchemaRequest(BaseModel):
    prompt: str


class PreviewRequest(BaseModel):
    columns: List[str]


class GenerateRequest(BaseModel):
    columns: List[str]
    rows: int = Field(gt=0, le=1_000_000)