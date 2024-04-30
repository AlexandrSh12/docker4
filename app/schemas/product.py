from pydantic import Field
from typing import Union, Annotated
from app.schemas.base import BaseSchema

class Product(BaseSchema):
    id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(min_length=2, max_length=30)]
    description: Annotated[Union[str, None], Field(max_length=500)] = None
    price: Annotated[float, Field(gt=0.0)]

    class ConfigDict:
        from_attributes=True
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "Kirill",
                "description": "Lorem ipsum",
                "price": 123.1
            }
        }

class CreateProduct(Product):
    id: None = None

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "name": "Kirill",
                "description": "Lorem ipsum",
                "price": 123.1
            }
        }