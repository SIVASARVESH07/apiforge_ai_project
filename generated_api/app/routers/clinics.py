# Router for clinics
from __future__ import annotations
from typing import Optional, List, Any
from fastapi import APIRouter, HTTPException, status, Header, Query, Path, Response
from app.models import *
from app.database import db

router = APIRouter(prefix="", tags=["Clinics"])

@router.get("/clinics", status_code=200)
async def get_clinics(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    items = db.list_all("clinics", limit=limit, offset=offset)
    total = len(db.get_table("clinics"))
    return {"items": items, "total": total, "limit": limit, "offset": offset}

@router.get("/clinics/{id}", status_code=200)
async def get_clinics_id(id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("clinics", id)
    if not item:
        raise HTTPException(status_code=404, detail="clinics not found")
    return item
