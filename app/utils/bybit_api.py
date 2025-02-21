from app.bybit.api import BybitUserApi
from app.database.models import BybitSecretKey


async def get_bybit_user_api() -> BybitUserApi:
    secret_key = await BybitSecretKey.get_last()
    return BybitUserApi(secret_key.secret_key)
