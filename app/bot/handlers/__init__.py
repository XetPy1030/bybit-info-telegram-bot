from aiogram import Router

from app.bot.handlers import balance
from app.bot.handlers import cookies

router = Router()
router.include_router(balance.router)
router.include_router(cookies.router)
