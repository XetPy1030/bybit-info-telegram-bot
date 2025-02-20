from app.utils.bybit_api import get_bybit_user_api
from app.database.models import Balance, BalanceItem
from app.config import AppConfig

async def update_asset_total_balance():
    api = await get_bybit_user_api()
    data = await api.get_asset_total_balance(quote_coin=AppConfig.DEFAULT_QUOTE_COIN)
    data_balance = data['result']
    balance = await Balance.create(
        quote_coin=AppConfig.DEFAULT_QUOTE_COIN,
        origin_total_balance=data_balance['originTotalBalance'],
        quote_total_balance=data_balance['quoteTotalBalance'],
    )
    for item in data_balance['totalBalanceItems']:
        await BalanceItem.create(
            balance=balance,
            account_type=item['accountType'],
            origin_balance=item['originBalance'],
            quote_balance=item['quoteBalance'],
        )
