from utils.mongo import convertObjectIdsToStr


class Model:
    @classmethod
    def from_dict(cls, source: dict): 
        source = convertObjectIdsToStr(source)
        ret = cls()
        for k, v in source.items():
            setattr(ret, k, v)
        return ret