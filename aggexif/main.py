import argparse
import subprocess
import json

from aggexif.aggregator import Aggregator
from aggexif.eixf_parser import parse_exif
from aggexif.filter_cond import gen_filter
from aggexif.printer import Printer


def run_exiftools(paths):
    commands = ['exiftool', '-j'] + paths
    result = subprocess.run(commands , stdout=subprocess.PIPE)
    return result.stdout


def arguments():
    parser = argparse.ArgumentParser("Aggregate EXIF")
    parser.add_argument("-w", "--width", help="print width", type=int, default=80)
    parser.add_argument("-l", "--lens", help="select lens", nargs='*')
    parser.add_argument("-c", "--camera", help="select camera", nargs='*')
    parser.add_argument("paths", help="images paths", nargs='*')
    args = parser.parse_args()
    if len(args.paths) == 0:
        print("Argument required")
        exit(1)
    return args


def main():
    args = arguments()
    result = run_exiftools(args.paths)
    files = json.loads(result)
    exifs = [parse_exif(f) for f in files]
    aggregator = Aggregator(exifs, lens_filter=gen_filter(args.lens), camera_filter=gen_filter(args.camera))
    printer = Printer(args.width)
    printer.print(aggregator)


if __name__ == '__main__':
    main()
