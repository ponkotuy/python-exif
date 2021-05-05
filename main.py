
import subprocess
import json


def run_exiftools(path):
    result = subprocess.run(['exiftool', '-j', path], stdout=subprocess.PIPE)
    return result.stdout


def main():
    result = run_exiftools("/home/yosuke/picture/20210503/raw/*.NEF")
    print(result)
    files = json.loads(result)
    lens = [f['LensID'] or f['LensModel'] for f in files]
    print(lens)


if __name__ == '__main__':
    main()
