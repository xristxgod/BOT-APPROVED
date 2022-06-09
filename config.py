import os
import logging


logger = logging.getLogger(__name__)


class Config:
    BOT_APPROVED_TOKEN = os.getenv("APPROVED_TB_TOKEN")
    SUPPORT_IDS = os.getenv("SUPPORT_IDS").split(",")

    BOT_API_URL = os.getenv("API_URL")
