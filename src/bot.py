from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.services.sender import Sender
from src.helper.utils import Utils
from src.helper.types import BodyUpdateTransaction
from config import Config, logger


storage = MemoryStorage()
bot = Bot(Config.BOT_APPROVED_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['cache'])
async def get_cache(message: types.Message):
    if message.from_user.id in Config.SUPPORT_IDS:
        await message.answer(
            text=Utils.process_repository_cache_for_text(message=await Sender.get_message_cache()),
            parse_mode=types.ParseMode.HTML,
        )


@dp.callback_query_handler(lambda x: x.data[:4] == "data")
async def process_message(callback_query: types.CallbackQuery):
    logger.error(f"PROCESS MESSAGE | Data: {callback_query.data}")
    _, method, user_id, network, tx_id = callback_query.data.split("-")
    await Sender.update_transaction(data=BodyUpdateTransaction(
        userId=user_id,
        nodeTransactionId=tx_id,
        network=network,
        outputs=Utils.outputs_parser(callback_query.message.text),
        text=Utils.process_text(callback_query.message.text, method=method),
        status=True if method == "approve" else False
    ))
