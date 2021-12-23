import json
import subprocess
from os.path import normpath
from typing import List, Dict, Iterable

from aggexif.aggeixf_argument import AggexifArgument
from aggexif.aggregator import Aggregator
from aggexif.exif_parser import parse_exif, Exif
from aggexif.filter_cond import gen_filter
from aggexif.printer import Printer
from aggexif.sqlite_cache import SQLiteExifCache


def run_exiftools(paths: List[str]) -> bytes:
    commands = ['exiftool', '-j'] + paths
    result = subprocess.run(commands, stdout=subprocess.PIPE)
    return result.stdout


def read_exifs(paths: List[str]) -> Dict[str, Exif]:
    if not paths:
        return {}
    exifs: Dict[str, Exif] = {}
    result = run_exiftools(paths)
    for f in json.loads(result):
        exifs[normpath(f['SourceFile'])] = parse_exif(f)
    return exifs


def read_cache_exifs(paths: Iterable[str], cache: SQLiteExifCache) -> Dict[str, Exif]:
    return cache.reads(paths)


def read_exif_process(args: AggexifArgument) -> List[Exif]:
    paths = {normpath(path) for path in args.paths}
    exifs = []
    if not args.ignore_cache:
        with SQLiteExifCache() as cache:
            exif_dic = read_cache_exifs(paths, cache)
            paths -= set(exif_dic.keys())
            exifs += exif_dic.values()
    read_result = read_exifs(list(paths))
    if args.cache:
        with SQLiteExifCache() as cache:
            cache.adds(read_result)
    exifs += read_result.values()
    return exifs


def main():
    args = AggexifArgument()
    exifs = read_exif_process(args)
    date_filter = args.date_filter()
    aggregator = Aggregator(
        exifs,
        lens_filter=gen_filter(args.lens),
        camera_filter=gen_filter(args.camera),
        date_filter=date_filter
    )
    printer = Printer(args.width, args.date_graph())
    printer.print(aggregator)


if __name__ == '__main__':
    main()
