from pydantic import BaseModel
from typing import Optional

class Marker_model(BaseModel):
    id: int
    url: str
    title: str
    description: Optional[str] | None = None
    category: Optional[str] | None = None
    status: Optional[str] | None = "active"
    
class BookMarkerUpdate_model(BaseModel):
    category: Optional[str] | None = None
    status: Optional[str] | None = "active"