
from rest.src.utils.mongo import convertObjectIdsToStr
from dataclasses import dataclass, field

@dataclass
class Visit(object):
    _id: str = field(init=True, default=None)
    visit_start: str = field(init=True, default=None)
    cost_per_min: int = field(init=True, default=None)
    visit_type: int = field(init=True, default=None)
    user: int = field(init=True, default=None)
    total_cost: int = field(init=True, default=None)
    visit_end: str = field(init=True, default=None)

    def from_dict(source: dict): 
        source = convertObjectIdsToStr(source)
        ret = Visit()
        for k, v in source.items():
            setattr(ret, k, v)
        return ret