from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message


router = Router()


@router.message(Command("start"))
async def start(message: Message):
    welcome_message = (
        "👋 Добро пожаловать в Bybit Info Bot!\n\n"
        "🤖 Этот бот поможет вам получать информацию о вашем балансе на Bybit.\n\n"
        "Доступные команды:\n"
        "📝 /start - показать это сообщение\n"
        "💰 /balance - получить информацию о балансе\n"
        "🔑 /set_secret_key - установить secret key и дату истечения\n" 
        "⏰ /expires_at - проверить когда истекает secret key\n\n"
        "❗️ Для начала работы необходимо установить secret key с помощью команды /set_secret_key\n"
        "Формат: /set_secret_key КЛЮЧ ГГГГ-ММ-ДД\n\n"
        "Если у вас возникли вопросы, обратитесь к документации или администратору."
    )
    await message.answer(welcome_message)

