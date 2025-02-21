from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    welcome_message = (
        "👋 Welcome to Bybit Info Bot!\n\n"
        "🤖 This bot will help you get information about your balance on Bybit.\n\n"
        "Available commands:\n"
        "📝 /start - show this message\n"
        "💰 /balance - get balance information\n"
        "🔑 /set_secret_key - set secret key and expiration date\n"
        "⏰ /expires_at - check when secret key expires\n\n"
        "❗️ To get started, you need to set a secret key using the /set_secret_key command\n"
        "Format: /set_secret_key KEY YYYY-MM-DD\n\n"
        "If you have any questions, please refer to the documentation or contact an administrator."
    )
    await message.answer(welcome_message)
