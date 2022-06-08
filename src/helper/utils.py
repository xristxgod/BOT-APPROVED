from datetime import datetime
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

    @staticmethod
    def get_outputs(outputs: List[Dict]) -> str:
        outputs_text = ""
        for output in outputs:
            address, amount = list(output.items())[0]
            outputs_text += f"{SYMBOL.get('user')}<b>{address}</b> на сумму: <b>{amount}</b>\n"
        return outputs_text[:-1]

    @staticmethod
    def process_repository_cache_for_text(message: Optional[Dict] = None) -> str:
        if message.get("message") == {}:
            return f"{SYMBOL.get('empty')} Репозиторий пуст!"
        elif message is None:
            return f"{SYMBOL.get('error')} Что-то пошло не так..."
        else:
            users = f"{SYMBOL.get('cache')} Репозиторий: \n\n"
            for user_id, networks_value in message.get("message").items():
                if len(networks_value.keys()) == 1:
                    title = "имеет не потвержденую транзакцию"
                else:
                    title = "имеет не потвержденные транзакции"
                user = f"{SYMBOL.get('userId')} Пользователь: {user_id} {title}\n"
                for network, data in networks_value.items():

                    time = datetime.utcfromtimestamp(data[0]).strftime('%Y-%m-%d %H:%M:%S')
                    user += (
                        f"{SYMBOL.get('memo')} Сеть: {network} | Время: {time} | Транзакция под номером: {data[1]}\n"
                        f"{Utils.get_outputs(data[2])}\n"
                    )
                users += user + "\n"
            return users
