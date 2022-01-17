
from dataclasses import dataclass, field
from database.models.current_visit import CurrentVisit
from database.models.visit_type import VisitType
from database.models.user import User
@dataclass
class Visit(CurrentVisit):
    _id: str = field(init=True, default=None)
    visit_start: str = field(init=True, default=None)
    cost_per_min: int = field(init=True, default=None)
    visit_type: VisitType = field(init=True, default=None)
    user: User = field(init=True, default=None)
    total_cost: int = field(init=True, default=None)
    visit_end: str = field(init=True, default=None)
    status: str = field(init=True, default=None)

    @classmethod
    def from_dict(cls, source: dict): 
        ret_visit = super().from_dict(source)
        if "user" not in source:
            return ret_visit
        user = User.from_dict(source["user"])
        ret_visit.user = user
        return ret_visit
        