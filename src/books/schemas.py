from pydantic import BaseModel, HttpUrl
from typing import Optional
from .models import Category, Status
import uuid


class Marker_model(BaseModel):
    uid: uuid.UUID
    url: HttpUrl
    title: str
    description: Optional[str] | None = None
    category: Optional[Category] | None = None
    status: Optional[Status] | None = "active"


class Marker_Create_model(BaseModel):
    url: HttpUrl
    title: str
    description: Optional[str] | None = None
    category: Optional[Category] | None = None
    status: Optional[Status] | None = "active"


class MarkerUpdate_model(BaseModel):
    url: HttpUrl
    title: str
    description: Optional[str] | None = None
    category: Optional[Category] | None = None
    status: Optional[Status] | None = "active"
