from typing import List, Any, Optional,Sequence,TypeVar,Generic
from pydantic import BaseModel

T = TypeVar("T")


class PageModel(BaseModel,Generic[T]):
    items: Sequence[T]
    has_next: Optional[bool]
    next_page: Optional[int]
    has_previous: Optional[bool]
    total: int
    pages: int
    
    class Config:
        arbitrary_types_allowed = True
