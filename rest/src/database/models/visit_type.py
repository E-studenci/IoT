
from utils.mongo import convertObjectIdsToStr
from dataclasses import dataclass, field

@dataclass
class VisitType(object):
    _id: str = field(init=True, default=None)
    visit_type: str = field(init=True, default=None)
    cost_per_min: int = field(init=True, default=None)
    rfid_scanner: str = field(init=True, default=None)

    def from_dict(source: dict): 
        source = convertObjectIdsToStr(source)
        ret = VisitType()
        for k, v in source.items():
            setattr(ret, k, v)
        return ret