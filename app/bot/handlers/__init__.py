from aiogram import Router

from app.bot.handlers import balance
from app.bot.handlers import cookies
from app.bot.middleware import AdminMiddleware

router = Router()
router.include_router(balance.router)
router.include_router(cookies.router)

router.message.middleware(AdminMiddleware())
