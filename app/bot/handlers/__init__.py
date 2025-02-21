from aiogram import Router

from app.bot.handlers import balance
from app.bot.handlers import secret_key
from app.bot.handlers import start
from app.bot.middleware import AdminMiddleware

router = Router()
router.include_router(balance.router)
router.include_router(secret_key.router)
router.include_router(start.router)

router.message.middleware(AdminMiddleware())
