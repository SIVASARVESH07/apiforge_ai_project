# Router for customers
from __future__ import annotations
from typing import Optional, List, Any
from fastapi import APIRouter, HTTPException, status, Header, Query, Path, Response
from app.models import *
from app.database import db

router = APIRouter(prefix="", tags=["Customers"])

@router.get("/customers", status_code=200)
async def get_customers(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    items = db.list_all("customers", limit=limit, offset=offset)
    total = len(db.get_table("customers"))
    return {"items": items, "total": total, "limit": limit, "offset": offset}

@router.post("/customers", status_code=201)
async def post_customers(payload: CustomerCreate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump() if hasattr(payload, "model_dump") else dict(payload)
    created = db.create("customers", data)
    return created

@router.get("/customers/{customer_id}", status_code=200)
async def get_customers_customer_id(customer_id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("customers", customer_id)
    if not item:
        raise HTTPException(status_code=404, detail="customers not found")
    return item

@router.delete("/customers/{customer_id}", status_code=204)
async def delete_customers_customer_id(customer_id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    deleted = db.delete("customers", customer_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="customers not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
