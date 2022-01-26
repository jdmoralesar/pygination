from typing import Optional,Sequence,TypeVar,Generic
from pydantic.generics import GenericModel

T = TypeVar("T")


class PageModel(GenericModel, Generic[T]):
    items: Sequence[T]
    has_next: Optional[bool]
    next_page: Optional[int]
    has_previous: Optional[bool]
    total: int
    pages: int

    class Config:
        arbitrary_types_allowed = True
