from api.utils.mongo import convertObjectIdsToStr


class Model(dict):
    def __init__(self) -> None:
        super().__init__(self.__dict__)

    @classmethod
    def from_dict(cls, source: dict): 
        source = convertObjectIdsToStr(source)
        ret = cls()
        for k, v in source.items():
            ret[k] = v
            setattr(ret, k, v)
        return ret
        