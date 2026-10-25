# Auto-generated Pydantic models from OpenAPI 3.1 specification
from __future__ import annotations
from typing import Optional, List, Any, Dict
from pydantic import BaseModel, Field
from datetime import datetime

class ErrorResponse(BaseModel):
    """Model for ErrorResponse"""
    detail: str
    status: int
    code: Optional[str] = None

class Patient(BaseModel):
    """Represents a patient record"""
    id: str
    title: str
    status: Optional[str] = None
    created_at: Optional[str] = None

class PatientCreate(BaseModel):
    """Payload for creating a new Patient"""
    title: str
    status: Optional[str] = None

class PatientUpdate(BaseModel):
    """Payload for updating an existing Patient"""
    title: Optional[str] = None
    status: Optional[str] = None

class PatientListResponse(BaseModel):
    """Paginated list of Patient records"""
    items: List[Patient]
    total: int
    limit: int
    offset: int
