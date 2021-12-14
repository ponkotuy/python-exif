from os.path import expanduser
from typing import Optional

from orjson import orjson

from aggexif.exif_parser import Exif
from aggexif.hdf5_string_cache import HDF5StringCache


class HDF5ExifCache:
    DIR_NAME = expanduser('~/.config/aggexif')

    def __init__(self):
        self.cache = HDF5StringCache(f'{self.DIR_NAME}/exif.hdf5', 'exif')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cache.close()

    def add(self, name: str, exif: Exif):
        self.cache.add(name, orjson.dumps(exif))

    def read(self, name: str) -> Optional[Exif]:
        raw = self.cache.read(name)
        return raw and Exif(**orjson.loads(raw))


def main():
    name = "picture/20211206/raw/a.NEF"
    exif = Exif("NIKKOR Z 50mm f/1.8 S", "Z7", 50)
    with HDF5ExifCache() as cache:
        cache.add(name, exif)
        print(cache.read(name))
        print(cache.read('notfound'))


if __name__ == '__main__':
    main()
