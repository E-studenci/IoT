
from dataclasses import dataclass, field
from database.models.model import Model

@dataclass
class User(Model):
    _id: str = field(init=True, default=None)
    surname: str = field(init=True, default=None)
    name: str = field(init=True, default=None)
    email: str = field(init=True, default=None)
    status: str = field(init=True, default=None)
    balance: int = field(init=True, default=None)
    card: str = field(init=True, default=None) ## TODO: add visit to user