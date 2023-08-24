import aiohttp
from .env import ENDPOINT

async def get_data():
    async with aiohttp.ClientSession as session:
        async with session.get(ENDPOINT) as response:
            return await response.json()