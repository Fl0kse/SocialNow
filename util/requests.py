from typing import Dict, Any
import aiohttp


async def async_request(url: str, method: str, headers: Dict[str: str] = None, json: Dict[Any, Any] = None):
    async with aiohttp.ClientSession() as session:
        resp = await session.request(method, url, json=json, headers=headers)
    return resp
