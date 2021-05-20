from dataclasses import dataclass

from aggexif import termgraph
from aggexif.aggregator import Aggregator
from aggexif.group import Group


@dataclass(frozen=True)
class Printer:
    width: int

    def print(self, aggregator: Aggregator):
        self.print_camera_list(aggregator.camera_groups())
        self.print_lens_list(aggregator.lens_groups())
        self.print_focal_length(aggregator.focal_length_groups())

    def print_lens_list(self, dic: dict):
        print('---- LENS LIST ----')
        self._print_dict(dic)

    def print_camera_list(self, dic: dict):
        print('---- CAMERA LIST ----')
        self._print_dict(dic)

    def print_focal_length(self, dic: dict):
        print('---- FOCAL LENGTH ----')
        self._print_grouping_count(dic)

    def _print_dict(self, dic, is_sort: bool = True):
        items = sorted(dic.items(), key=lambda x: -x[1]) if is_sort else dic.items()
        termgraph.render(items, width=self.width)

    def _print_grouping_count(self, groups: [Group]):
        dic = {}
        for group in groups:
            if group.count != 0:
                dic[group.name()] = group.count
        self._print_dict(dic, False)
