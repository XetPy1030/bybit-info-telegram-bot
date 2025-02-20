from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "bybitsecretkey" ALTER COLUMN "secret_key" TYPE VARCHAR(511) USING "secret_key"::VARCHAR(511);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "bybitsecretkey" ALTER COLUMN "secret_key" TYPE VARCHAR(255) USING "secret_key"::VARCHAR(255);"""
