import aiohttp

from src.helper.types import BodyUpdateTransaction
from config import Config, logger


class Sender:

    URL_UPDATE = Config.BOT_API_URL + "/bot/update"

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
    async def get_message_cache():
        pass
