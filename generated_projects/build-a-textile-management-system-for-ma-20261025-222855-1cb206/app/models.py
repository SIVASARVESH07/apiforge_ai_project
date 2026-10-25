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

class User(BaseModel):
    """Represents a user record"""
    id: str
    title: str
    status: Optional[str] = None
    created_at: Optional[str] = None

class UserCreate(BaseModel):
    """Payload for creating a new User"""
    title: str
    status: Optional[str] = None

class UserUpdate(BaseModel):
    """Payload for updating an existing User"""
    title: Optional[str] = None
    status: Optional[str] = None

class UserListResponse(BaseModel):
    """Paginated list of User records"""
    items: List[User]
    total: int
    limit: int
    offset: int

class Order(BaseModel):
    """Represents a order record"""
    id: str
    title: str
    status: Optional[str] = None
    created_at: Optional[str] = None

class OrderCreate(BaseModel):
    """Payload for creating a new Order"""
    title: str
    status: Optional[str] = None

class OrderUpdate(BaseModel):
    """Payload for updating an existing Order"""
    title: Optional[str] = None
    status: Optional[str] = None

class OrderListResponse(BaseModel):
    """Paginated list of Order records"""
    items: List[Order]
    total: int
    limit: int
    offset: int

class Product(BaseModel):
    """Represents a product record"""
    id: str
    title: str
    status: Optional[str] = None
    created_at: Optional[str] = None

class ProductCreate(BaseModel):
    """Payload for creating a new Product"""
    title: str
    status: Optional[str] = None

class ProductUpdate(BaseModel):
    """Payload for updating an existing Product"""
    title: Optional[str] = None
    status: Optional[str] = None

class ProductListResponse(BaseModel):
    """Paginated list of Product records"""
    items: List[Product]
    total: int
    limit: int
    offset: int

class Customer(BaseModel):
    """Represents a customer record"""
    id: str
    title: str
    status: Optional[str] = None
    created_at: Optional[str] = None

class CustomerCreate(BaseModel):
    """Payload for creating a new Customer"""
    title: str
    status: Optional[str] = None

class CustomerUpdate(BaseModel):
    """Payload for updating an existing Customer"""
    title: Optional[str] = None
    status: Optional[str] = None

class CustomerListResponse(BaseModel):
    """Paginated list of Customer records"""
    items: List[Customer]
    total: int
    limit: int
    offset: int
