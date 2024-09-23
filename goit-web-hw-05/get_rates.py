import sys
import aiohttp
import asyncio

from datetime import datetime, timedelta


CURR1 = "USD"
CURR2 = "EUR"


class HttpError(Exception):
    pass
pass

async def request(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as resp:
                if resp.status == 200:
                    result = await resp.json()
                    return result
                else:
                    raise HttpError(f"Error status: {resp.status} for {url}")
        except (aiohttp.ClientConnectorError, aiohttp.InvalidURL) as err:
            raise HttpError(f'Connection error: {url}', str(err))


async def get_exchange_rates(date: str) -> dict:
    url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
    response = await request(url)
    rates = {}
    for exchange_rate in response["exchangeRate"]:
        currency = exchange_rate["currency"]
        if currency not in (CURR1, CURR2):
            continue
        rates[currency] = {
            "sale": exchange_rate["saleRate"],
            "purchase": exchange_rate["purchaseRate"],
        }
    return {date: rates}


async def main(index_day):
    days = int(index_day)
    results = []
    while days > 0:
        date = (datetime.now() - timedelta(days=days)).strftime("%d.%m.%Y")
        try:
            rates = await get_exchange_rates(date)
            results.append(rates)
        except HttpError as err:
            print(err)
        days -= 1
    return results



if __name__ == "__main__":
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    rates = asyncio.run(main(sys.argv[1]))
    print(rates)