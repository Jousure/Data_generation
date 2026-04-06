from fastapi import APIRouter
from app.models.request import SchemaRequest
from app.core.schema_generator import generate_enhanced_schema
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor

router = APIRouter()

@router.post("/")
async def generate_schema(req: SchemaRequest):
    topic = req.prompt.strip()
    
    # Use enhanced schema generator with intelligent data type mapping
    schema = generate_enhanced_schema(topic)
    
    # Convert to expected format with proper data types
    columns = []
    for col in schema:
        columns.append({
            "name": col["name"],
            "type": col["type"]
        })
    
    response = {
        "title": req.prompt.strip()[:60] if req.prompt.strip() else "Custom Dataset",
        "columns": columns[:12]  # Limit to 12 columns for better UX
    }
    
    return response
