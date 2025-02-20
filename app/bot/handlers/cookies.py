from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.database.models import BybitSecretKey


router = Router()


@router.message(Command("set_cookies"))
async def set_cookies(message: Message):
    try:
        secret_key = message.text.split(" ")[1]
    except IndexError:
        await message.answer("Please provide a secret key")
        return

    try:
        await BybitSecretKey.create(secret_key=secret_key)
        await message.answer("✅ Cookies successfully set")
    except Exception as e:
        await message.answer(f"❌ Error setting cookies: {str(e)}")
