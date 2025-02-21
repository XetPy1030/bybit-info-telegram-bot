from app.database.models import BybitSecretKey
from app.config import AppConfig
from app.bot.instance import bot


async def notify_about_expired_cookies(bybit_secret_key: BybitSecretKey, minutes: int):
    for admin_id in AppConfig.ADMIN_IDS:
        await bot.send_message(
            admin_id,
            f"🚨 Your cookies will expire in {minutes} minutes",
        )
