from typing import Optional, List, Dict
from dataclasses import dataclass

import emoji


SYMBOL = {
    "error": emoji.emojize(":thinking_face:"),
    "empty": emoji.emojize(":shushing_face:"),
    "cache": emoji.emojize(":eyes:"),
    "userId": emoji.emojize(":id:", language='alias'),
    "memo": emoji.emojize(":memo:", language='alias'),
    "user": emoji.emojize(":bust_in_silhouette:"),
    "approve": emoji.emojize(":check_mark_button:"),
    "reject": emoji.emojize(":cross_mark:")
}


@dataclass
class BodyUpdateTransaction:
    support_id: int
    userId: int
    nodeTransactionId: int
    network: str
    status: bool
    outputs: Optional[List[Dict]] = None
    text: Optional[str] = None

    @property
    def to_json(self):
        if self.outputs is None:
            del self.outputs
        return self.__dict__
