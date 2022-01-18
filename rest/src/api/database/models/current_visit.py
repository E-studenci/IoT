from dataclasses import dataclass, field

from api.database.models.model import Model
from api.database.models.visit_type import VisitType

@dataclass
class CurrentVisit(Model):
    _id: str = field(init=True, default=None)
    visit_start: str = field(init=True, default=None)
    cost_per_min: int = field(init=True, default=None)
    visit_type: VisitType = field(init=True, default=None)

    @classmethod
    def from_dict(cls, source: dict): 
        ret_current_visit = super().from_dict(source)
        if "visit_type" not in source:
            return ret_current_visit
        visit_type = VisitType.from_dict(source["visit_type"])
        ret_current_visit.visit_type = visit_type
        return ret_current_visit