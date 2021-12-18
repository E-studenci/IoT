

class User(object):
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
    
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
        return self.login

    def __eq__(self, other):
        if isinstance(other, User):
            return self.get_id() == other.get_id()
        return False

    def __ne__(self, other):
        equal = self.__eq__(other)
        return not equal