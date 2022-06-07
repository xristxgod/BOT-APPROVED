import os
import logging


logger = logging.getLogger(__name__)


class Config:
    BOT_APPROVED_TOKEN = os.getenv("APPROVED_TB_TOKEN")
    SUPPORT_ID = int(os.getenv("SUPPORT_ID"))

    APPROVED_DOMAIN = os.getenv("APPROVED_DOMAIN")
    APPROVED_AUTH_BEARER_TOKEN = os.getenv("APPROVED_AUTH_BEARER_TOKEN")

    BOT_API_URL = os.getenv("API_URL")
