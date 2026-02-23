from fastapi import APIRouter
from app.models.request import SchemaRequest

router = APIRouter()

@router.post("/")
def generate_schema(req: SchemaRequest):
    topic = req.prompt.strip()

    return {
        "title": topic[:60] if topic else "Custom Dataset",
        "columns": [
            "name",
            "category",
            "description",
            "value",
            "created_at"
        ]
    }
