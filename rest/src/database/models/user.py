
from dataclasses import dataclass, field
from database.models.model import Model
from database.models.visit import Visit
@dataclass
class User(Model):
    _id: str = field(init=True, default=None)
    surname: str = field(init=True, default=None)
    name: str = field(init=True, default=None)
    email: str = field(init=True, default=None)
    status: str = field(init=True, default=None)
    balance: int = field(init=True, default=None)
    card: str = field(init=True, default=None) ## TODO: add visit to user
    current_visit: Visit = field(init=True, default=None)

    @classmethod
    def from_dict(cls, source: dict): 
        ret_user = super().from_dict(source)
        if "current_visit" not in source:
            return ret_user
        visit = Visit.from_dict(source["current_visit"])
        ret_user.current_visit = visit
        return ret_user
