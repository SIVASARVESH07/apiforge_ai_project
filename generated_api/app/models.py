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

class Item(BaseModel):
    """Represents a item record"""
    id: str
    title: str
    status: Optional[str] = None
    created_at: Optional[str] = None

class ItemCreate(BaseModel):
    """Payload for creating a new Item"""
    title: str
    status: Optional[str] = None

class ItemUpdate(BaseModel):
    """Payload for updating an existing Item"""
    title: Optional[str] = None
    status: Optional[str] = None

class ItemListResponse(BaseModel):
    """Paginated list of Item records"""
    items: List[Item]
    total: int
    limit: int
    offset: int
