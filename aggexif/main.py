import argparse
import subprocess
import json
from collections import Iterable
from os.path import normpath
from typing import List, Dict

from aggexif.aggregator import Aggregator
from aggexif.exif_parser import parse_exif, Exif
from aggexif.hdf5_exif_cache import HDF5ExifCache
from aggexif.filter_cond import gen_filter
from aggexif.printer import Printer


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


def read_cache_exifs(paths: Iterable[str], cache: HDF5ExifCache) -> Dict[str, Exif]:
    exif_dic = {}
    for path in paths:
        exif = cache.read(path)
        if exif is not None:
            exif_dic[path] = exif
    return exif_dic


def read_exif_process(args: argparse.Namespace) -> List[Exif]:
    paths = {normpath(path) for path in args.paths}
    exifs = []
    if not args.ignore_cache:
        with HDF5ExifCache() as cache:
            exif_dic = read_cache_exifs(paths, cache)
            paths -= set(exif_dic.keys())
            exifs += exif_dic.values()
    read_result = read_exifs(list(paths))
    if args.cache:
        with HDF5ExifCache() as cache:
            for name, exif in read_result.items():
                cache.add(name, exif)
    exifs += read_result.values()
    return exifs


def arguments():
    parser = argparse.ArgumentParser("Aggregate EXIF")
    parser.add_argument("-w", "--width", help="print width", type=int, default=80)
    parser.add_argument("-l", "--lens", help="select lens", nargs='*')
    parser.add_argument("-c", "--camera", help="select camera", nargs='*')
    parser.add_argument("-a", "--cache", help="save exif in cache", action='store_true')
    parser.add_argument("--ignore-cache", help="ignore cache", action='store_true')
    parser.add_argument("paths", help="images paths", nargs='*')
    args = parser.parse_args()
    if len(args.paths) == 0:
        print("Argument required")
        exit(1)
    return args


def main():
    args = arguments()
    exifs = read_exif_process(args)
    aggregator = Aggregator(exifs, lens_filter=gen_filter(args.lens), camera_filter=gen_filter(args.camera))
    printer = Printer(args.width)
    printer.print(aggregator)


if __name__ == '__main__':
    main()
