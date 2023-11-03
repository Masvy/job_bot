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
                chat_member = await event.bot.get_chat_member(
                    chat_id='-1001360482054', user_id=event.from_user.id)
                result = await session.execute(select(User).where(User.user_id == event.from_user.id))
                user = result.scalar()

                if chat_member.status != 'left':
                    if user is not None:
                        pass
                    else:
                        user = User(
                            user_id=event.from_user.id,
                            user_name=event.from_user.username
                        )
                        await session.merge(user)
                else:
                    await event.answer('Для продолжения вы должны '
                                       'подписаться на канал: @Kanzoboz',
                                       show_alert=True)
                    return

        return await handler(event, data)
