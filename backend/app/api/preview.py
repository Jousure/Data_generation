from fastapi import APIRouter
from app.models.request import PreviewRequest
from app.core.column_map import generate_value

router = APIRouter()

@router.post("/")
def preview_data(req: PreviewRequest):
    preview = [
        {c: generate_value(c) for c in req.columns}
        for _ in range(100)
    ]
    return {
        "columns": req.columns,
        "preview": preview
    }
