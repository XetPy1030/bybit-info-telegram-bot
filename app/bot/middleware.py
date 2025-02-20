from aiogram import BaseMiddleware
from aiogram.dispatcher.event.bases import CancelHandler
from aiogram.types import TelegramObject
from typing import Callable

from app.config import AppConfig


class AdminMiddleware(BaseMiddleware):
    async def __call__(self, handler: Callable, event: TelegramObject, data: dict):
        if event.from_user.id not in AppConfig.ADMIN_IDS:
            raise CancelHandler()
        return await handler(event, data)
