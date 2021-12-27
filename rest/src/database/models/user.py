
from dataclasses import dataclass, field
from database.models.model import Model

@dataclass
class User(Model):
    _id: str = field(init=True, default=None)
    login: str = field(init=True, default=None)
    password: int = field(init=True, default=None)
    surname: str = field(init=True, default=None)
    name: str = field(init=True, default=None)
    email: str = field(init=True, default=None)
    status: str = field(init=True, default=None)
    balance: str = field(init=True, default=None)

    @property
    def is_active(self):
        return True

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self._id

    def __eq__(self, other):
        if isinstance(other, User):
            return self.get_id() == other.get_id()
        return False

    def __ne__(self, other):
        equal = self.__eq__(other)
        return not equal