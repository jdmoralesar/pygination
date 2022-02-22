import math
from typing import List, Any

from sqlalchemy.orm import Query
from pygination.errors import PaginationError


class Page:
    def __init__(self, items: List[Any], page: int, size: int, total: int) -> None:

        self.pages = int(math.ceil(total / float(size)))
        if page > 0 and page > self.pages - 1:
            raise PaginationError("Page is greater than the total number of pages in the query.")
        self.page = page
        self.size = size
        self.items = items
        self.previous_page = None
        self.next_page = None
        self.has_previous = page > 0
        if self.has_previous:
            self.previous_page = page - 1
        previous_items = page * size
        self.has_next = previous_items + len(items) < total

        if self.has_next and len(self.items) < self.size:
            raise PaginationError("Invalid query. There are duplicate entries in this page of the query.")

        if self.has_next:
            self.next_page = page + 1
        self.total = total

    def __repr__(self) -> str:
        repr_string_list = []
        if self.has_previous:
            repr_string_list.append(f"Previous page was {self.previous_page}")
        else:
            repr_string_list.append("Previous page does not exist")

        if self.has_next:
            repr_string_list.append(f"Next page is {self.next_page}")
        else:
            repr_string_list.append("Next page does not exist")

        repr_string_list.append(f"Total number of pages {self.pages}")
        repr_string = ". ".join(repr_string_list)
        return repr_string


def paginate(query: Query, page: int, size: int) -> Page:
    if page < 0:
        raise AttributeError("page needs to be >= 0")
    if size <= 0:
        raise AttributeError("size needs to be >= 1")
    total = query.order_by(None).count()
    query_page = page * size
    items = query.limit(size).offset(query_page).all()
    return Page(items, page, size, total)
