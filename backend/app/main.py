from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.schema import router as schema_router
from app.api.preview import router as preview_router
from app.api.generate import router as generate_router

app = FastAPI(title="Dataset Generator")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(schema_router, prefix="/schema")
app.include_router(preview_router, prefix="/preview")
app.include_router(generate_router, prefix="/generate")

@app.get("/")
def health():
    return {"status": "ok"}

