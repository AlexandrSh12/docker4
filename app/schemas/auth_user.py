from pydantic import Field
from datetime import date
from typing import Union, Annotated
from app.schemas.base import BaseSchema
from app.schemas.trip import Trip
from pydantic import BaseModel

class AuthUser(BaseSchema):
    login: Annotated[str, Field(min_length=2, max_length=30)]
    name: Annotated[str, Field(min_length=2, max_length=30)]
    age: Annotated[int, Field(gt=0)]
    height: Annotated[int, Field(gt=0)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": "1",
                "login": "Balaev",
                "name": "Kirill",
                "age": "15",
                "height": "150"
            }
        }

class CreateAuthUser(AuthUser):
    id: None = None
    password: Annotated[str, Field(min_length=6, max_length=30)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "login": "Balaev",
                "name": "Kirill",
                "age": "15",
                "height": "150",
                "password": "qwerty123"
            }
        }

class SignInAuthUser(BaseModel):
    login: Annotated[str, Field(min_length=2, max_length=30)]
    password: Annotated[str, Field(min_length=6, max_length=30)]

    class ConfigDict:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "login": "Balaev",
                "password": "qwerty123"
            }
        }