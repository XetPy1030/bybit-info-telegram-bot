from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "balance" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "quote_coin" VARCHAR(255) NOT NULL,
    "origin_total_balance" DOUBLE PRECISION NOT NULL,
    "quote_total_balance" DOUBLE PRECISION NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);
        CREATE TABLE IF NOT EXISTS "balanceitem" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "account_type" VARCHAR(255) NOT NULL,
    "origin_balance" DOUBLE PRECISION NOT NULL,
    "quote_balance" DOUBLE PRECISION NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "balance_id" INT NOT NULL REFERENCES "balance" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "balance";
        DROP TABLE IF EXISTS "balanceitem";"""
