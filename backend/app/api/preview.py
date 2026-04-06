from fastapi import APIRouter
from app.models.request import PreviewRequest
from app.core.generator import generate_value, get_domain_context

router = APIRouter()

@router.post("/")
def preview_data(req: PreviewRequest):
    domain = get_domain_context(req.columns)
    preview = [
        {c: generate_value(c, domain) for c in req.columns}
        for _ in range(100)
    ]
    return {
        "columns": req.columns,
        "preview": preview
    }
