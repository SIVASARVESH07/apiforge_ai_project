# Router for students
from __future__ import annotations
from typing import Optional, List, Any
from fastapi import APIRouter, HTTPException, status, Header, Query, Path, Response
from app.models import *
from app.database import db

router = APIRouter(prefix="", tags=["Students"])

@router.post("/students", status_code=201)
async def createStudent(payload: StudentCreate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump() if hasattr(payload, "model_dump") else dict(payload)
    created = db.create("students", data)
    return created

@router.get("/students", status_code=200)
async def listStudents(limit: int = Query(20, ge=1, le=100), offset: int = Query(0, ge=0), authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    items = db.list_all("students", limit=limit, offset=offset)
    total = len(db.get_table("students"))
    return {"items": items, "total": total, "limit": limit, "offset": offset}

@router.get("/students/{id}", status_code=200)
async def getStudentById(id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    item = db.get_by_id("students", id)
    if not item:
        raise HTTPException(status_code=404, detail="students not found")
    return item

@router.put("/students/{id}", status_code=200)
async def updateStudent(id: str, payload: StudentUpdate, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    data = payload.model_dump(exclude_unset=True) if hasattr(payload, "model_dump") else dict(payload)
    updated = db.update("students", id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="students not found")
    return updated

@router.delete("/students/{id}", status_code=204)
async def deleteStudent(id: str, authorization: Optional[str] = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid bearer token")
    deleted = db.delete("students", id)
    if not deleted:
        raise HTTPException(status_code=404, detail="students not found")
    return Response(status_code=status.HTTP_204_NO_CONTENT)
