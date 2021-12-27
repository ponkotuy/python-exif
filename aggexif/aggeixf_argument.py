import argparse
import os
import sys
from enum import Enum, auto

from aggexif.filter_cond import DateFilter


class DateGraph(Enum):
    YEARLY = auto()
    MONTHLY = auto()
    DAILY = auto()


def path_filter(path) -> bool:
    return os.path.isfile(path)


class AggexifArgument:
    def __init__(self):
        self.args = _gen_parser().parse_args()
        self.width = self.args.width
        self.ignore_cache = self.args.ignore_cache
        self.cache = self.args.cache
        self.lens = self.args.lens
        self.camera = self.args.camera
        if len(self.args.paths) == 0:
            if sys.stdin.isatty():
                print("Argument required")
                exit(1)
            else:
                self.paths = list(filter(path_filter, (line[:-1] for line in sys.stdin)))

    def date_filter(self):
        year = list(map(int, self.args.year))
        month = list(map(int, self.args.month))
        day = list(map(int, self.args.day))
        return DateFilter(year, month, day)

    def date_graph(self) -> DateGraph:
        dates = (
            (self.args.daily, DateGraph.DAILY),
            (self.args.monthly, DateGraph.MONTHLY),
            (self.args.yearly, DateGraph.YEARLY),
            (True, DateGraph.YEARLY)  # Default
        )
        return next(filter(lambda x: x[0], dates))[1]


def _gen_parser():
    parser = argparse.ArgumentParser("Aggregate EXIF")
    parser.add_argument("-w", "--width", help="print width", type=int, default=80)
    parser.add_argument("-l", "--lens", help="select lens", nargs='+')
    parser.add_argument("-c", "--camera", help="select camera", nargs='+')
    parser.add_argument("--year", help="select year", type=int, nargs='+', default=[])
    parser.add_argument("--month", help="select month", type=int, nargs='+', default=[])
    parser.add_argument("--day", help="select day of month", type=int, nargs='+', default=[])
    parser.add_argument("--yearly", help="view yearly graph", action='store_true')
    parser.add_argument("--monthly", help="view monthly graph", action='store_true')
    parser.add_argument("--daily", help="view daily graph", action='store_true')
    parser.add_argument("-a", "--cache", help="save exif in cache", action='store_true')
    parser.add_argument("--ignore-cache", help="ignore cache", action='store_true')
    parser.add_argument("paths", help="images paths", nargs='*')
    return parser
