
import sys
import subprocess
import json
from python_exif.printer import *


def run_exiftools(paths):
    commands = ['exiftool', '-j'] + paths
    result = subprocess.run(commands , stdout=subprocess.PIPE)
    return result.stdout


def arguments():
    return sys.argv[1:]


def main():
    result = run_exiftools(arguments())
    files = json.loads(result)
    print_camera_list(files)
    print_lens_list(files)
    print_focal_length(files)


if __name__ == '__main__':
    main()
