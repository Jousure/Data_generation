from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

from app.api.schema import router as schema_router
from app.api.preview import router as preview_router
from app.api.generate import router as generate_router
from app.api.data_types import router as data_types_router

app = FastAPI(
    title="Dataset Generator",
    # Increase timeout for large dataset generation
    timeout=300  # 5 minutes
)

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (generated CSVs)
app.mount("/generated", StaticFiles(directory="generated"), name="generated")

# ROUTERS
app.include_router(schema_router, prefix="/schema")
app.include_router(preview_router, prefix="/preview")
app.include_router(generate_router, prefix="/generate")
app.include_router(data_types_router, prefix="/data-types")

@app.get("/")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        timeout_keep_alive=300,  # 5 minutes
        timeout_graceful_shutdown=30
    )

