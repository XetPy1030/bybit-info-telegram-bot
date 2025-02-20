import asyncio
import structlog

from app.utils.logging import setup_logger

async def main():
    setup_logger()
    logger = structlog.get_logger(__name__)
    logger.info("Starting application")

    from app.database import init as init_database
    await init_database()

    from app.bot.instance import dp
    from app.bot.handlers import router
    dp.include_router(router)
    logger.info("Bot handlers included")
    
    from app.background_tasks import run_background_tasks
    await run_background_tasks()

    logger.info("Starting bot polling...")
    from app.bot.instance import bot
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
