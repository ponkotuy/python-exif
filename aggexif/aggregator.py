from datetime import datetime

from aggexif.exif_parser import Exif
from aggexif.filter_cond import FilterCond, FILTER_NONE, DateFilter, DATE_FILTER_NONE
from aggexif.group import Group

FOCAL_LENGTHS = [10, 15, 20, 24, 28, 35, 40, 45, 50, 60, 70, 85, 105, 135, 200, 300, 400, 500, 600, 800, 1000, 1200]


class Aggregator:
    def __init__(
            self,
            data: [Exif],
            lens_filter: FilterCond = FILTER_NONE,
            camera_filter: FilterCond = FILTER_NONE,
            date_filter: DateFilter = DATE_FILTER_NONE
    ):
        lens = set(x.lens for x in data)
        self.lens_filter = lens_filter.contains_match_value(lens)
        cameras = set(x.camera for x in data)
        self.camera_filter = camera_filter.contains_match_value(cameras)
        self.date_filter = date_filter
        self.data = [
            x for x in data if (self.lens_filter.filter(x.lens)
                                and self.camera_filter.filter(x.camera)
                                and self.date_filter.filter(x.shooting_time))
        ]

    def lens_groups(self):
        return grouping_count(x.lens for x in self.data)

    def camera_groups(self):
        return grouping_count(x.camera for x in self.data)

    def focal_length_groups(self):
        lengths = (x.focal_length for x in self.data if x.focal_length)
        return grouping_range_count(lengths, FOCAL_LENGTHS)

    def yearly_groups(self):
        return grouping_count(str(x.shooting_time.year) for x in self.data)

    def monthly_groups(self):
        return grouping_count(x.shooting_time.strftime('%Y/%m') for x in self.data)

    def daily_groups(self):
        return grouping_count(x.shooting_time.strftime('%Y/%m/%d') for x in self.data)


def grouping_range_count(data, separators) -> [Group]:
    groups = [Group(x, y, 0) for x, y in zip([None] + separators, separators + [None])]
    for num in data:
        next((g for g in groups if g.has(num))).incr()
    return groups


def grouping_count(ary):
    result = {}
    for x in ary:
        if x:
            result[x] = result.get(x, 0) + 1
    return result
