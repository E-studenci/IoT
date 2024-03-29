from dataclasses import dataclass, field

from api.database.models.model import Model


@dataclass
class VisitType(Model):
    _id: str = field(init=True, default=None)
    visit_type: str = field(init=True, default=None)
    cost_per_min: int = field(init=True, default=None)
    rfid_scanner: str = field(init=True, default=None)
