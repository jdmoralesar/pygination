# Introduction 
This module will help you paginate results from any database if you use the sqlalchemy object Query.
The PageModel pydantic model can be easily integrated with FastAPI and swagger.  

# Getting Started

Here is a brief example of how to use this code.


```
from pygination import paginate
from pygination.models import PageModel

query = db.query(models.City)

if country_id is not None:
    query = query.filter(models.City.country_id == country_id)
    
page = paginate(query, offset, limit)

print(page)
# Previous page does not exist. Next page is 2. Total number of pages 4

page_model = PageModel.from_orm(page)
```