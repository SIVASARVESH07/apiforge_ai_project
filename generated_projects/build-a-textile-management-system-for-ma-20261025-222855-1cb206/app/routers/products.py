# Router for products
from __future__ import annotations
from typing import Optional, List, Any
from fastapi import APIRouter, HTTPException, status, Header, Query, Path, Response
from app.models import *
from app.database import db

router = APIRouter(prefix="", tags=["Products"])

@router.get("/products", status_code=200)
async def get_products(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    items = db.list_all("products", limit=limit, offset=offset)
    total = len(db.get_table("products"))
    return {"items": items, "total": total, "limit": limit, "offset": offset}

@router.post("/products", status_code=201)
async def post_products(payload: ProductCreate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump() if hasattr(payload, "model_dump") else dict(payload)
    created = db.create("products", data)
    return created

@router.get("/products/{product_id}", status_code=200)
async def get_products_product_id(product_id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("products", product_id)
    if not item:
        raise HTTPException(status_code=404, detail="products not found")
    return item

@router.delete("/products/{product_id}", status_code=204)
async def delete_products_product_id(product_id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    deleted = db.delete("products", product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="products not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
