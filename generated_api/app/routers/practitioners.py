# Router for practitioners
from __future__ import annotations
from typing import Optional, List, Any
from fastapi import APIRouter, HTTPException, status, Header, Query, Path, Response
from app.models import *
from app.database import db

router = APIRouter(prefix="", tags=["Practitioners"])

@router.get("/practitioners", status_code=200)
async def get_practitioners(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    items = db.list_all("practitioners", limit=limit, offset=offset)
    total = len(db.get_table("practitioners"))
    return {"items": items, "total": total, "limit": limit, "offset": offset}

@router.get("/practitioners/{id}", status_code=200)
async def get_practitioners_id(id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("practitioners", id)
    if not item:
        raise HTTPException(status_code=404, detail="practitioners not found")
    return item
