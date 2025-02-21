from datetime import datetime

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.database.models import BybitSecretKey


router = Router()


@router.message(Command("set_cookies"))
async def set_cookies(message: Message):
    try:
        args = message.text.split(" ")[1:]
        if not args:
            await message.answer("Please provide a secret key")
            return
            
        secret_key = args[0]
        expires_at = None
        if len(args) > 1:
            try:
                # Parse expires_at from ISO format string
                expires_at = datetime.fromisoformat(args[1])
            except (ValueError, IndexError):
                await message.answer("❌ Invalid expires_at format. Use ISO format (YYYY-MM-DD HH:MM:SS)")
                return

        await BybitSecretKey.create(secret_key=secret_key, expires_at=expires_at)
        await message.answer("✅ Cookies successfully set")
    except Exception as e:
        await message.answer(f"❌ Error setting cookies: {str(e)}")
