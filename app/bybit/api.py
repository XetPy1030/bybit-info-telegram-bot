import httpx


class BybitUserApi:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
    
    async def get_asset_total_balance(self, quote_coin: str):
        """
        Ex: {'ret_code': 0, 'ret_msg': 'success', 'result': {'totalBalanceItems': [{'accountType': 'ACCOUNT_TYPE_C2C_YBB', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_FIXED_RATE_LOAN', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_LAUNCHPOOL', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_PLEDGE_LOANS', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_PRE_MARKET_TRADING', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_UNIFIED', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_FUND', 'originBalance': '0.0000893', 'quoteBalance': '0.000000000910948045', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_INVESTMENT', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_COPY_TRADE_ALL', 'originBalance': '2915.44723992', 'quoteBalance': '0.029740436319835185', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_COPY_TRADE', 'originBalance': '2915.44723992', 'quoteBalance': '0.029740436319835185', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_COPY_PRO', 'originBalance': '0', 'quoteBalance': '0', 'status': 0}, {'accountType': 'ACCOUNT_TYPE_BOT', 'originBalance': '154.75', 'quoteBalance': '0.001578602575096088', 'status': 0}], 'originTotalBalance': '3070.19732922', 'quoteTotalBalance': '0.031319039805879318', 'status': 0}, 'ext_code': '', 'ext_info': None, 'time_now': '1740074570.561436'}
        """
        url = "https://api2.bybit.com/v3/private/cht/asset-show/asset-total-balance"
        async with httpx.AsyncClient(timeout=20) as client:
            response = await client.get(url, params={'quoteCoin': quote_coin}, cookies=self.cookies)
            response.raise_for_status()
            self.raise_for_bybit_error(response)
            return response.json()

    @staticmethod
    def raise_for_bybit_error(response: httpx.Response):
        data = response.json()
        if data['ret_code'] != 0:
            raise httpx.HTTPStatusError(
                message=data['ret_msg'],
                request=response.request,
                response=response,
            )
    
    @property
    def cookies(self):
        return {
            'secure-token': self.secret_key,
        }
