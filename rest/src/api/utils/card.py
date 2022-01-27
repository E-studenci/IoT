from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Card():
    rfid: str = field(init=True, default=None)
    scanned: datetime = field(init=True, default=None)

LAST_SCANNED_CARD = Card()