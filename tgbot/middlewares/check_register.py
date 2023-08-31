from typing import Any, Awaitable, Callable, Dict, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker

from database.create_table import User


class RegisterCheck(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]):
            session_maker: sessionmaker = data['session_maker']
            async with session_maker() as session:
                async with session.begin():
                    result = await session.execute(select(User).where(User.user_id == event.from_user.id))
                    user = result.scalar()

                    if user is not None:
                        pass
                    else:
                        user = User(
                                user_id=event.from_user.id,
                                user_name=event.from_user.username
                            )
                        await session.merge(user)

            return await handler(event, data)
