from app.config import AppConfig
from app.bot.instance import bot

async def handle_exception(e: Exception):
    import traceback
    stacktrace = ''.join(traceback.format_exception(type(e), e, e.__traceback__))
    for admin_id in AppConfig.ADMIN_IDS:
        await bot.send_message(admin_id, f"❌ Error: `{e}`\n\nStacktrace:\n```\n{stacktrace}\n```")
