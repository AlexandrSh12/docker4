from fastapi import APIRouter, status, Response, Path, Depends, Request
from fastapi.templating import Jinja2Templates
from typing import Union, List
from app.schemas.default_response import DefaultResponse
from app.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
import hashlib

from app.models.auth_user import AuthUser
from app.schemas.auth_user import AuthUser as AuthUserSchema, CreateAuthUser, SignInAuthUser
from app.repository import crud
from app.repository.auth_user import get_user_by_password_and_login

router = APIRouter(
    prefix="/api/auth_user", 
    tags=["authUser"]
)

responses = {
    status.HTTP_404_NOT_FOUND: {"model": DefaultResponse, "description": "Item not found"}
}

templates = Jinja2Templates(directory="./app/templates")

def get_password_hash(password):
    return hashlib.md5(password.encode("utf-8")).hexdigest()

@router.post("/sign_up", status_code=status.HTTP_201_CREATED)
async def sign_up_user(authUser: CreateAuthUser, db: AsyncSession = Depends(get_db)):
    authUser.password = get_password_hash(authUser.password)
    authUser: AuthUser = await crud.create(AuthUser, authUser, db)

    return authUser

@router.post("/sign_in", response_model=Union[AuthUserSchema, DefaultResponse])
async def get_driver(data: SignInAuthUser, resquest: Request, response: Response, db: AsyncSession = Depends(get_db)):
    authUser: AuthUser = await get_user_by_password_and_login(get_password_hash(data.password), data.login, db)
    if authUser == None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return DefaultResponse(success=False, message="User not found")
    
    context = {"request": resquest, "login": authUser.login, "age": authUser.age, "height": authUser.height}

    return templates.TemplateResponse("users.html", context)