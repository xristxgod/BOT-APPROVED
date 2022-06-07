import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from src.helper.utils import Utils
from config import Config, logger


storage = MemoryStorage()
bot = Bot(Config.BOT_APPROVED_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        (
            "<b> Welcome to bot </b>"
        ),
        parse_mode=types.ParseMode.HTML
    )


@dp.callback_query_handler(lambda x: x.data[:4] == "data")
async def process_message(callback_query: types.CallbackQuery):
    logger.error(f"PROCESS MESSAGE | Data: {callback_query.data}")
    _, method, user_id, network, tx_id = callback_query.data.split("-")
    await bot.edit_message_text(
        text=Utils.process_text(callback_query.message.text, method=method),
        parse_mode=types.ParseMode.HTML,
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id)
