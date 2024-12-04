from typing import Optional, Sequence, TypeVar, Generic
from pydantic import BaseModel, ConfigDict


T = TypeVar("T")


class PageModel(BaseModel, Generic[T]):
    items: Sequence[T]
    page: Optional[int] = None
    size: int = 0
    total: int
    pages: int
    next_page: Optional[int] = None
    previous_page: Optional[int] = None

    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)