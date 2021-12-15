import re
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True)
class Exif:
    lens: str
    camera: str
    focal_length: Optional[int]
    shooting_time: datetime
    shooting_time_utc: datetime


EXIF_TIME_PARSER = '%Y:%m:%d %H:%M:%S'
EXIF_TIME_PARSER_UTC = f'{EXIF_TIME_PARSER}%z'


def parse_exif(obj) -> Exif:
    lens = obj.get('LensID') or obj.get('LensModel')
    camera = obj.get('Model')
    focal = parse_length(obj.get('FocalLengthIn35mmFormat') or obj.get('FocalLength35efl'))
    shooting_time = parse_time(obj.get('DateTimeOriginal'))
    shooting_time_utc = parse_utc(obj.get('GPSDateTime'))
    focal = None if focal == 0 else focal
    return Exif(lens, camera, focal, shooting_time, shooting_time_utc)


def parse_length(length) -> int:
    if not length:
        return 0
    result = re.findall(r"\d+", length)
    return int(result[0]) if result else 0


def parse_time(string: str):
    return datetime.strptime(string, EXIF_TIME_PARSER)


def parse_utc(string: str):
    return datetime.strptime(string, EXIF_TIME_PARSER_UTC)
