import sqlite3
from dataclasses import dataclass, asdict
from os.path import expanduser
from typing import Optional, Iterable

from aggexif.exif_parser import Exif


class SQLiteExifCache:
    DIR_NAME = expanduser('~/.config/aggexif')
    CREATE_TABLE = "create table if not exists exifs (" \
                   "`path` text not null," \
                   "version integer not null," \
                   "lens text not null," \
                   "camera text not null," \
                   "focal_length integer," \
                   "unique(`path`))"
    VERSION = 1

    def __init__(self):
        self.conn = sqlite3.connect(f'{self.DIR_NAME}/exif.db')
        self.one_exec(self.CREATE_TABLE)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.conn.close()

    def one_exec(self, sql: str):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def adds(self, dic: dict[str, Exif]):
        cur = self.conn.cursor()
        exifs = [asdict(ExifRow(name, self.VERSION, exif.lens, exif.camera, exif.focal_length)) for name, exif in dic.items()]
        cur.executemany(f"replace into exifs values (:path, :version, :lens, :camera, :focal_length)", exifs)
        self.conn.commit()

    def reads(self, names: Iterable[str]):
        if not names:
            return []
        cur = self.conn.cursor()
        csv = ', '.join(f"'{name}'" for name in names)
        result = {}
        for row in cur.execute(f'select * from exifs where path in ({csv}) and version = {self.VERSION}'):
            result[row[0]] = Exif(row[2], row[3], row[4])
        return result


@dataclass(frozen=True)
class ExifRow:
    path: str
    version: int
    lens: str
    camera: str
    focal_length: Optional[int]


def main():
    name = "picture/20211206/raw/a.NEF"
    exif = Exif("NIKKOR Z 50mm f/1.8 S", "Z7", 50)
    with SQLiteExifCache() as cache:
        cache.adds({name: exif})
        print(cache.reads([name]))
        print(cache.reads(['notfound']))


if __name__ == '__main__':
    main()
