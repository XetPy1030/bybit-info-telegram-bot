import asyncio
import logging

from app.bybit.api import BybitUserApi

logging.basicConfig(level=logging.DEBUG)


async def main():
    user_api = BybitUserApi(secret_key='eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0Mjc5MTgwOTcsImIiOjAsInAiOjMsInVhIjoiIiwiZ2VuX3RzIjoxNzQwMDY4OTg4LCJleHAiOjE3NDAzMjgxODgsIm5zIjoiIiwiZXh0Ijp7IlN0YXRpb24tVHlwZSI6IiIsIm1jdCI6IjE3Mzg4NjgxMzkiLCJzaWQiOiJCWUJJVCJ9LCJkIjpmYWxzZSwic2lkIjoiIn0.bXSqIWT9Ph-k5TG_IH7JfW79Y69N2e4D4aqnsu6J5jSERqY8S6TrQQWi09Sa2Q6YNhkVn6GuktVcq6SVWdcctQ')
    print(await user_api.get_asset_total_balance(quote_coin='BTC'))


if __name__ == "__main__":
    asyncio.run(main())
