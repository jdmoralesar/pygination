import math
from typing import List, Any

from sqlalchemy.orm import Query


class Page(object):
    def __init__(self, items: List[Any] , offset: int, limit: int, total: int) -> None:
        self.items = items
        self.previous_page = None
        self.next_page = None
        self.has_previous = offset > 1
        if self.has_previous:
            self.previous_page = offset - 1
        previous_items = (offset - 1) * limit
        self.has_next = previous_items + len(items) < total
        if self.has_next:
            self.next_page = offset + 1
        self.total = total
        self.pages = int(math.ceil(total / float(limit)))

    def __repr__(self) -> str:
        repr_string = ""
        if self.has_previous:
            repr_string += f"Previous page was {self.previous_page}. "
        else:
            repr_string += "Previous page does not exist. "

        if self.has_next:
            repr_string += f"Next page is {self.next_page}. "
        else:
            repr_string += "Next page does not exist. "

        repr_string += f"Total number of pages {self.pages}"

        return repr_string


def paginate(query: Query, offset: int, limit: int) -> Page:
    if offset <= 0:
        raise AttributeError("offset needs to be >= 1")
    if limit <= 0:
        raise AttributeError("limit needs to be >= 1")
    total = query.order_by(None).count()
    items = query.limit(limit).offset((offset - 1) * limit).all()
    return Page(items, offset, limit, total)
