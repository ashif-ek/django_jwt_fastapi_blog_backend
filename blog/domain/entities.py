from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class PostEntity:
    title: str
    content: str
    author_id: int
    id: Optional[int] = None
    slug: Optional[str] = None
    image: Optional[str] = None
    published: bool = True
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
