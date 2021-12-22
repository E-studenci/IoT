
from rest.src.utils.mongo import convertObjectIdsToStr

class User(object):
    def __init__(self, _id=None, login=None, password=None, surname=None, name=None, email=None, status=None, balance=None) -> None:
        self._id = _id
        self.login = login
        self.password = password
        self.surname = surname
        self.name = name
        self.email = email
        self.status = status
        self.balance = balance

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

    def from_dict(source: dict): 
        source = convertObjectIdsToStr(source)
        ret = User()
        for k, v in source.items():
            setattr(ret, k, v)
        return ret