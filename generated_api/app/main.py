# Main entrypoint for Item Management API
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.routers import items

app = FastAPI(
    title="Item Management API",
    version="1.0.0",
    description="""Generated API based on requirements: design a supermarket management api...""",
    openapi_url="/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "service": "api-forge"}

app.include_router(items.router)
