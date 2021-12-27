import re
import time
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
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
    lens: Optional[str] = obj.get('LensID') or obj.get('LensModel')
    if lens is None or 'Unknown' in lens:
        lens = None
    camera = obj.get('Model') or 'Unknown'
    focal = parse_length(obj.get('FocalLengthIn35mmFormat') or obj.get('FocalLength35efl'))
    shooting_time = parse_shooting_time(obj)
    shooting_time_utc = parse_utc(obj.get('GPSDateTime'))
    focal = None if focal == 0 else focal
    return Exif(lens, camera, focal, shooting_time, shooting_time_utc)


def parse_shooting_time(obj):
    return parse_time(obj.get('DateTimeOriginal')) or parse_profile_date_time(obj) or datetime(1, 1, 1, 0, 0)


def parse_profile_date_time(obj):
    """Parse EXIF shooting time for DJI MAVIC"""
    dt = parse_time(obj.get('ProfileDateTime'))
    if dt is None:
        return None
    else:
        return dt - timedelta(seconds=time.timezone)


def parse_length(length) -> int:
    if not length:
        return 0
    result = re.findall(r"\d+", length)
    return int(result[0]) if result else 0
