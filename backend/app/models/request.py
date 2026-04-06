from pydantic import BaseModel, Field
from typing import List, Dict, Any


class SchemaRequest(BaseModel):
    prompt: str


class PreviewRequest(BaseModel):
    columns: List[Dict[str, Any]]  # Changed to handle new schema format


class GenerateRequest(BaseModel):
    columns: List[Dict[str, Any]]  # Changed to handle new schema format
    rows: int = Field(gt=0, le=1_000_000)