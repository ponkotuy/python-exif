import json
from dataclasses import asdict
from os.path import expanduser

from aggexif.eixf_parser import Exif
from aggexif.hdf5_string_cache import HDF5StringCache


class ExifCache:
    DIR_NAME = expanduser('~/.config/aggexif')

    def __init__(self):
        self.cache = HDF5StringCache(f'{self.DIR_NAME}/exif.hdf5', 'exif')

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cache.close()

    def add(self, name, exif):
        self.cache.add(name, json.dumps(asdict(exif)))

    def read(self, name):
        return json.loads(self.cache.read(name))


def main():
    cache = ExifCache()
    name = "picture/20211206/raw/a.NEF"
    exif = Exif("NIKKOR Z 50mm f/1.8 S", "Z7", 50)
    cache.add(name, exif)
    print(cache.read(name))


if __name__ == '__main__':
    main()
