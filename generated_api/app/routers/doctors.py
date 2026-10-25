# Router for doctors
from __future__ import annotations
from typing import Optional, List, Any
from fastapi import APIRouter, HTTPException, status, Header, Query, Path, Response
from app.models import *
from app.database import db

router = APIRouter(prefix="", tags=["Doctors"])

@router.get("/doctors", status_code=200)
async def listDoctors(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    items = db.list_all("doctors", limit=limit, offset=offset)
    total = len(db.get_table("doctors"))
    return {"items": items, "total": total, "limit": limit, "offset": offset}

@router.post("/doctors", status_code=201)
async def createDoctor(payload: DoctorCreate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump() if hasattr(payload, "model_dump") else dict(payload)
    created = db.create("doctors", data)
    return created

@router.get("/doctors/{id}", status_code=200)
async def getDoctorById(id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("doctors", id)
    if not item:
        raise HTTPException(status_code=404, detail="doctors not found")
    return item

@router.put("/doctors/{id}", status_code=200)
async def updateDoctor(id: str, payload: DoctorUpdate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump(exclude_unset=True) if hasattr(payload, "model_dump") else dict(payload)
    updated = db.update("doctors", id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="doctors not found")
    return updated

@router.patch("/doctors/{id}", status_code=200)
async def patchDoctor(id: str, payload: DoctorUpdate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump(exclude_unset=True) if hasattr(payload, "model_dump") else dict(payload)
    updated = db.update("doctors", id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="doctors not found")
    return updated

@router.delete("/doctors/{id}", status_code=204)
async def deleteDoctor(id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    deleted = db.delete("doctors", id)
    if not deleted:
        raise HTTPException(status_code=404, detail="doctors not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/doctors/{id}/appointments", status_code=200)
async def getDoctorAppointments(id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("doctors", id)
    if not item:
        raise HTTPException(status_code=404, detail="doctors not found")
    return item
