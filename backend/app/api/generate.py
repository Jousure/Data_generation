from fastapi import APIRouter
from app.models.request import GenerateRequest
from app.utils.file_writer import write_csv_streaming

router = APIRouter()

@router.post("/")
def generate_dataset(req: GenerateRequest):
    """
    Generate dataset using streaming approach for better performance with large datasets.
    """
    file_path = write_csv_streaming(req.columns, req.rows)
    return {"file": file_path}
