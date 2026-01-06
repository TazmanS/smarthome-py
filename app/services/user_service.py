from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User as UserModel
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, session: AsyncSession):
        self.repo = UserRepository(session)

    async def get_user(self, user_id: int) -> Optional[UserModel]:
        return await self.repo.get_user_by_id(user_id)
