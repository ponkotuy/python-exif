from dataclasses import dataclass
from enum import Enum, auto


class FilterType(Enum):
    PARTIAL_MATCH = auto()
    PARTIAL_MATCH_NOT = auto()
    ENTIRE_MATCH = auto()
    ENTIRE_MATCH_NOT = auto()
    NONE = auto()

@dataclass(frozen=True)
class FilterCond:
    type: FilterType
    values: [str]

    def filter(self, value: str) -> bool:
        if self.type == FilterType.PARTIAL_MATCH:
            return any(v in value for v in self.values)
        elif self.type == FilterType.PARTIAL_MATCH_NOT:
            return all(v not in value for v in self.values)
        elif self.type == FilterType.ENTIRE_MATCH:
            return value in self.values
        elif self.type == FilterType.ENTIRE_MATCH_NOT:
            return value not in self.values
        else:
            return True

    def contains_match_value(self, values: set):
        if self.type in (FilterType.ENTIRE_MATCH, FilterType.ENTIRE_MATCH_NOT, FilterType.NONE):
            return self
        if set(self.values) & values:
            if self.type == FilterType.PARTIAL_MATCH:
                return FilterCond(FilterType.ENTIRE_MATCH, self.values)
            else:
                return FilterCond(FilterType.ENTIRE_MATCH_NOT, self.values)
        else:
            return self

FILTER_NONE = FilterCond(FilterType.NONE, [])

def gen_filter(args: [str]):
    return FilterCond(FilterType.PARTIAL_MATCH, args) if args else FILTER_NONE

