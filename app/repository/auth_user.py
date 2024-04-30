from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.auth_user import AuthUser

async def get_user_by_password_and_login(password: str, login: str, db: AsyncSession):
    stmt = select(AuthUser).where(AuthUser.password == password).where(AuthUser.login == login)
    result = await db.execute(stmt)
    return result.scalars().first()