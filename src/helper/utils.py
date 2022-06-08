from typing import Optional, List, Dict

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

    @staticmethod
    def outputs_parser(text) -> Optional[List[Dict]]:
        try:
            text_list: List = text.split("\n")
            count = 0
            for t in text_list:
                if t == "":
                    break
                count += 1
            outputs_list = text_list[count+1:]
            finally_outputs: List = []
            for outputs in outputs_list:
                address, amount_network = outputs.split(" на сумму: ")
                finally_outputs.append({
                    address[1:]: amount_network.split(" ")[0]
                })
            return finally_outputs
        except:
            return None
