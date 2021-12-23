from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import Optional


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

    def filter(self, value: Optional[str]) -> bool:
        if value is None:
            return False
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


@dataclass(frozen=True)
class DateFilter:
    years: [int]
    months: [int]
    days: [int]

    def filter(self, time: datetime):
        """
        Examples:
            >>> DATE_FILTER_NONE.filter(datetime.now())
            True
        """
        if self.years and time.year not in self.years:
            return False
        if self.months and time.month not in self.months:
            return False
        if self.days and time.day not in self.days:
            return False
        return True


DATE_FILTER_NONE = DateFilter([], [], [])


def gen_filter(args: [str]):
    return FilterCond(FilterType.PARTIAL_MATCH, args) if args else FILTER_NONE
