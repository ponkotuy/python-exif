import os
import sqlite3
from dataclasses import dataclass, asdict
from datetime import datetime
from os.path import expanduser
from typing import Optional, Iterable

from aggexif.exif_parser import Exif


class SQLiteExifCache:
    DIR_NAME = expanduser('~/.config/aggexif')
    DROP_TABLE = "drop table if exists exifs"
    CREATE_TABLE = "create table if not exists exifs (" \
                   "`path` text not null," \
                   "version integer not null," \
                   "lens text," \
                   "camera text not null," \
                   "focal_length integer," \
                   "shooting_time datetime not null," \
                   "shooting_time_utc datetime," \
                   "unique(`path`))"
    VERSION = 2

    def __init__(self):
        os.makedirs(self.DIR_NAME, exist_ok=True)
        self.conn = sqlite3.connect(f'{self.DIR_NAME}/exif.db')
        self.migration()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        self.conn.close()

    def migration(self):
        version = self.read_version()
        if version == 0:
            self.one_exec(self.CREATE_TABLE)
        elif version < self.VERSION:
            self.one_exec(self.DROP_TABLE)
            self.one_exec(self.CREATE_TABLE)

    def read_version(self):
        # If not exists table, return 0
        cur = self.conn.cursor()
        try:
            cur.execute(f'select version from exifs limit 1')
        except sqlite3.Error:
            return 0
        version = cur.fetchone()
        cur.close()
        if version is None:
            return 0
        return version[0]

    def one_exec(self, sql: str):
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def adds(self, dic: dict[str, Exif]):
        cur = self.conn.cursor()
        exifs = [
            asdict(
                ExifRow(
                    name,
                    self.VERSION,
                    exif.lens,
                    exif.camera,
                    exif.focal_length,
                    exif.shooting_time,
                    exif.shooting_time_utc
                )
            ) for name, exif in dic.items()]
        sql = "replace into exifs values (" \
              ":path," \
              ":version," \
              ":lens," \
              ":camera," \
              ":focal_length," \
              ":shooting_time," \
              ":shooting_time_utc" \
              ")"
        cur.executemany(sql, exifs)
        self.conn.commit()

    def reads(self, names: Iterable[str]) -> dict[str, Exif]:
        if not names:
            return {}
        cur = self.conn.cursor()
        csv = ', '.join(f"'{name}'" for name in names)
        result = {}
        for row in cur.execute(f'select * from exifs where path in ({csv}) and version = {self.VERSION}'):
            result[row[0]] = Exif(
                row[2],
                row[3],
                row[4],
                datetime.fromisoformat(row[5]),
                row[6] and datetime.fromisoformat(row[6])
            )
        return result


@dataclass(frozen=True)
class ExifRow:
    path: str
    version: int
    lens: str
    camera: str
    focal_length: Optional[int]
    shooting_time: datetime
    shooting_time_utc: Optional[datetime]


def main():
    name = "picture/20211206/raw/a.NEF"
    exif = Exif("NIKKOR Z 50mm f/1.8 S", "Z7", 50, datetime.now(), datetime.utcnow())
    with SQLiteExifCache() as cache:
        cache.adds({name: exif})
        print(cache.reads([name]))
        print(cache.reads(['notfound']))


if __name__ == '__main__':
    main()
