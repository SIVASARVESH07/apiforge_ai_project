# Router for items
from __future__ import annotations
from typing import Optional, List, Any
from fastapi import APIRouter, HTTPException, status, Header, Query, Path, Response
from app.models import *
from app.database import db

router = APIRouter(prefix="", tags=["Items"])

@router.get("/items", status_code=200)
async def get_items(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    items = db.list_all("items", limit=limit, offset=offset)
    total = len(db.get_table("items"))
    return {"items": items, "total": total, "limit": limit, "offset": offset}

@router.post("/items", status_code=201)
async def post_items(payload: ItemCreate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump() if hasattr(payload, "model_dump") else dict(payload)
    created = db.create("items", data)
    return created

@router.get("/items/{item_id}", status_code=200)
async def get_items_item_id(item_id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("items", item_id)
    if not item:
        raise HTTPException(status_code=404, detail="items not found")
    return item

@router.delete("/items/{item_id}", status_code=204)
async def delete_items_item_id(item_id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    deleted = db.delete("items", item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="items not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
