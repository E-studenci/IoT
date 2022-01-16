
from dataclasses import dataclass, field
from database.models.model import Model

@dataclass
class Visit(Model):
    _id: str = field(init=True, default=None)
    visit_start: str = field(init=True, default=None)
    cost_per_min: int = field(init=True, default=None)
    visit_type: str = field(init=True, default=None)
    user: str = field(init=True, default=None)
    total_cost: int = field(init=True, default=None)
    visit_end: str = field(init=True, default=None)