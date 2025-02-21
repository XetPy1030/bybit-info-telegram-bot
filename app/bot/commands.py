from aiogram.types import BotCommand


async def setup_commands(bot):
    await bot.set_my_commands([
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="balance", description="Get the balance of Bybit"),
        BotCommand(command="set_secret_key", description="Set the secret key and expiration date (format: /set_secret_key KEY YYYY-MM-DD)"),
        BotCommand(command="expires_at", description="Check when the secret key expires"),
        BotCommand(command="update_balance", description="Update balance information"),
    ])
