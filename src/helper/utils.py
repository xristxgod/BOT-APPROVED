from typing import List

from src.helper.types import SYMBOL


class Utils:
    @staticmethod
    def process_text(text: str, method: str) -> str:
        text_list: List = text.split("\n")
        if method == "approve":
            text_list[0] = f"{SYMBOL.get(method)} <b>Заявка одобрена</b>"
        else:
            text_list[0] = f"{SYMBOL.get(method)} <b>Заявка отклонена</b>"
        finally_text = ""
        for t in text_list:
            finally_text += f"{t}\n"
        return finally_text
