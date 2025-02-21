from datetime import datetime

from app.bybit.api import BybitUserApi
from app.database.models import BybitSecretKey


async def get_bybit_secret_key():
    secret_key = await BybitSecretKey.all().order_by("-updated_at").first()
    return secret_key.secret_key


async def update_bybit_secret_key(secret_key: str, expires_at: datetime | None = None):
    await BybitSecretKey.create(secret_key=secret_key, expires_at=expires_at)


async def get_bybit_user_api() -> BybitUserApi:
    secret_key = await get_bybit_secret_key()
    return BybitUserApi(secret_key)
