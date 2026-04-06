from fastapi import APIRouter
from app.models.request import PreviewRequest
from app.core.generator import generate_value, get_domain_context

router = APIRouter()

@router.post("/")
def preview_data(req: PreviewRequest):
    domain = get_domain_context([col["name"] for col in req.columns])
    preview = [
        {col["name"]: generate_value(col["type"], domain) for col in req.columns}
        for _ in range(10)  # Generate 10 preview rows
    ]
    return {
        "columns": req.columns,
        "preview": preview
    }
