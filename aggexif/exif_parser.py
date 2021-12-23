import re
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from aggexif.exif_time_parser import parse_time, parse_utc


@dataclass(frozen=True)
class Exif:
    lens: Optional[str]
    camera: str
    focal_length: Optional[int]
    shooting_time: datetime
    shooting_time_utc: Optional[datetime]


def parse_exif(obj) -> Exif:
    lens = obj.get('LensID') or obj.get('LensModel')
    if 'Unknown' in lens:
        lens = None
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
