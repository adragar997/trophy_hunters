import aiohttp
import asyncio

class AsyncFetchData:
    async def fetch_data(self, session, url, params):
        async with session.get(url, params=params) as response:
            return await response.json()

    async def create_session(self, url, params):
        async with aiohttp.ClientSession() as session:
            tasks = [asyncio.create_task(self.fetch_data(session,url, params))]
            data = await asyncio.gather(*tasks)
            return data[0]