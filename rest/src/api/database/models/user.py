from dataclasses import dataclass, field


from api.database.models.current_visit import CurrentVisit
from api.database.models.model import Model

@dataclass
class User(Model):
    _id: str = field(init=True, default=None)
    surname: str = field(init=True, default=None)
    name: str = field(init=True, default=None)
    email: str = field(init=True, default=None)
    status: str = field(init=True, default=None)
    card: str = field(init=True, default=None)
    current_visit: CurrentVisit = field(init=True, default=None)

    @classmethod
    def from_dict(cls, source: dict): 
        ret_user = super().from_dict(source)
        if "current_visit" not in source:
            return ret_user
        visit = CurrentVisit.from_dict(source["current_visit"])
        ret_user.current_visit = visit
        return ret_user
