from dataclasses import dataclass
from typing import TypeVar

from aggexif import termgraph
from aggexif.aggeixf_argument import DateGraph
from aggexif.aggregator import Aggregator
from aggexif.group import Group


T = TypeVar('T')


@dataclass(frozen=True)
class Printer:
    width: int
    dately: DateGraph

    def print(self, aggregator: Aggregator):
        self.print_camera_list(aggregator.camera_groups())
        self.print_lens_list(aggregator.lens_groups())
        self.print_focal_length(aggregator.focal_length_groups())
        if self.dately == DateGraph.YEARLY:
            self.print_yearly(aggregator.yearly_groups())
        elif self.dately == DateGraph.MONTHLY:
            self.print_monthly(aggregator.monthly_groups())
        else:
            self.print_daily(aggregator.daily_groups())

    def print_lens_list(self, dic: dict):
        print_partition('LENS LIST')
        self._print_dict(dic)

    def print_camera_list(self, dic: dict):
        print_partition('CAMERA LIST')
        self._print_dict(dic)

    def print_focal_length(self, dic: dict):
        print_partition('FOCAL LENGTH')
        self._print_grouping_count(dic)

    def print_yearly(self, dic: dict):
        print_partition('YEAR')
        self._print_ordered_dict(dic)

    def print_monthly(self, dic: dict):
        print_partition('MONTH')
        self._print_ordered_dict(dic)

    def print_daily(self, dic: dict):
        print_partition('DAY')
        self._print_ordered_dict(dic)

    def _print_dict(self, dic, is_sort: bool = True):
        items = sorted(dic.items(), key=lambda x: -x[1]) if is_sort else dic.items()
        termgraph.render(items, width=self.width)

    def _print_ordered_dict(self, dic):
        items = sorted(dic.items(), key=lambda x: x[0])
        termgraph.render(items, width=self.width)

    def _print_grouping_count(self, groups: [Group]):
        dic = {}
        for group in groups:
            if group.count != 0:
                dic[group.name()] = group.count
        self._print_dict(dic, False)


def print_partition(name):
    print(f'---- {name} ----')
