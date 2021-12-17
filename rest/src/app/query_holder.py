

class QueryHolder:
    def _add_query(self, name, function):
        setattr(self, name, function)
