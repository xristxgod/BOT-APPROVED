from typing import Optional, List, Dict
from dataclasses import dataclass

import emoji


SYMBOL = {
    "approve": emoji.emojize(":check_mark:"),
    "reject": emoji.emojize(":cross_mark:")
}


@dataclass
class BodyUpdateTransaction:
    userId: int
    nodeTransactionId: int
    network: str
    status: bool
    outputs: Optional[List[Dict]] = None

    @property
    def to_json(self):
        if self.outputs is None:
            del self.outputs
        return self.__dict__
