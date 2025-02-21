from datetime import datetime

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.database.models import BybitSecretKey
from app.utils.datetime import format_dt

router = Router()


@router.message(Command("set_secret_key"))
async def set_secret_key(message: Message):
    try:
        args = message.text.split(" ")[1:]
        if not args:
            await message.answer("Please provide a secret key.\n\n"
                                 "To get the secret key:\n"
                                 "1. Go to Bybit website (www.bybit.com)\n"
                                 "2. Open browser Developer Tools (F12)\n"
                                 "3. Find 'secret_key' in cookies\n"
                                 "4. Copy the value of 'secret_key' cookie")
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
        await message.answer("✅ Secret key successfully set")
    except Exception as e:
        await message.answer(f"❌ Error setting secret key: {str(e)}")


@router.message(Command("expires_at"))
async def expires_at(message: Message):
    secret_key = await BybitSecretKey.get_last()
    if not secret_key:
        await message.answer("❌ Secret key not found")
        return
    await message.answer(f"🕒 Secret key expires at: {format_dt(secret_key.expires_at)}")
