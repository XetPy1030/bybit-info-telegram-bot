from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from app.bybit.consts import ACCOUNT_TYPE_NAMES
from app.database.models import Balance, BalanceItem
from app.utils.datetime import format_dt

router = Router()


@router.message(Command("balance"))
async def balance(message: Message):
    balance = await Balance.all().order_by("-created_at").last()
    if balance is None:
        await message.answer("Balance not found")
        return

    text = f"💰 Balance Report 💰\n\n" \
           f"💵 Total Balance: {balance.origin_total_balance:.8f} USDT ({balance.quote_total_balance:.2f} {balance.quote_coin})\n" \
           f"📅 Created at: {format_dt(balance.created_at)}\n\n" \
           f"📊 Breakdown by Account Type:\n" + \
           "\n".join(f"• {ACCOUNT_TYPE_NAMES.get(item.account_type, item.account_type)}: {item.origin_balance:.8f} USDT ({item.quote_balance:.2f} {balance.quote_coin})"
                    for item in await balance.items.all() if item.quote_balance > 0)

    await message.answer(text)
