# Main entrypoint for User Management API
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users
from app.routers import orders
from app.routers import products
from app.routers import customers

app = FastAPI(
    title="User Management API",
    version="1.0.0",
    description="""Generated API based on requirements: Build a textile management system for managing fabrics, yarn, inventory, suppliers, and customer ord...""",
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

app.include_router(users.router)
app.include_router(orders.router)
app.include_router(products.router)
app.include_router(customers.router)
