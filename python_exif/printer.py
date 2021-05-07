import re
from dataclasses import dataclass
from typing import Optional

from python_exif import termgraph


@dataclass
class Group:
    min: Optional[int]
    max: Optional[int]
    count: int

    def incr(self):
        self.count += 1

    def has(self, value: int) -> bool:
        return (self.min is None or self.min < value) and \
               (self.max is None or value <= self.max)

    def name(self) -> str:
        return f'{self.min or ""}-{self.max or ""}'


def grouping_count(ary):
    result = {}
    for x in ary:
        if x:
            result[x] = result.get(x, 0) + 1
    return result


def grouping_range_count(data, separators) -> [Group]:
    groups = [Group(x, y, 0) for x, y in zip([None] + separators, separators + [None])]
    for num in data:
        next((g for g in groups if g.has(num))).incr()
    return groups


def print_dict(dic, is_sort: bool = True):
    items = sorted(dic.items(), key=lambda x: -x[1]) if is_sort else dic.items()
    termgraph.render(items, 80)


def print_grouping_count(groups: [Group]):
    dic = {}
    for group in groups:
        if group.count != 0:
            dic[group.name()] = group.count
    print_dict(dic, False)


def print_lens_list(data):
    lens = [f.get('LensID') or f.get('LensModel') for f in data]
    lens_count = grouping_count(lens)
    print('---- LENS LIST ----')
    print_dict(lens_count)


def print_camera_list(data):
    cameras = [f.get('Model') for f in data]
    camera_count = grouping_count(cameras)
    print('---- CAMERA LIST ----')
    print_dict(camera_count)


FOCAL_LENGTHS = [10, 15, 20, 24, 28, 35, 40, 45, 50, 60, 70, 85, 105, 135, 200, 300, 400, 500, 600, 800, 1000, 1200]

def parse_length(length) -> int:
    if not length:
        return 0
    result = re.findall(r"\d+", length)
    return int(result[0]) if result else 0


def print_focal_length(data):
    lengths = [parse_length(f.get('FocalLengthIn35mmFormat') or f.get('FocalLength35efl')) for f in data]
    lengths = filter(lambda x: x != 0, lengths)
    length_groups = grouping_range_count(lengths, FOCAL_LENGTHS)
    print('---- FOCAL LENGTH ----')
    print_grouping_count(length_groups)
