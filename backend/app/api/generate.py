from fastapi import APIRouter
from app.models.request import GenerateRequest
from app.core.generator import generate_rows
from app.utils.file_writer import write_csv

router = APIRouter()

@router.post("/")
def generate_dataset(req: GenerateRequest):
    data = generate_rows(req.columns, req.rows)
    file_path = write_csv(data)
    return {"file": file_path}
