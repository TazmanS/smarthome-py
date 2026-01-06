from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.user import User as UserModel


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: int) -> Optional[UserModel]:
        result = await self.session.execute(select(UserModel).where(UserModel.id == user_id))
        user = result.scalars().first()
        return user
