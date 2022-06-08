from typing import Optional, Dict

import aiohttp

from src.helper.types import BodyUpdateTransaction
from config import Config, logger


class Sender:

    URL_UPDATE = Config.BOT_API_URL + "/bot/update"
    URL_REPOSITORY_CACHE = Config.BOT_API_URL + "/repository/cache"

    @staticmethod
    async def update_transaction(data: BodyUpdateTransaction) -> bool:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(
                        url=Sender.URL_UPDATE,
                        json=data.to_json
                ) as response:
                    logger.error(f"SEND TO SITE: {response.ok}")
                    return bool((await response.json()).get("status"))
        except Exception as error:
            logger.error(f"ERROR: {error}")
            return False

    @staticmethod
    async def get_message_cache() -> Optional[Dict]:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                        url=Sender.URL_REPOSITORY_CACHE
                ) as response:
                    logger.error(f"SEND TO SITE: {response.ok}")
                    return await response.json()
        except Exception as error:
            logger.error(f"ERROR: {error}")
            return None

