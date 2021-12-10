import re
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Exif:
    lens: str
    camera: str
    focal_length: Optional[int]


def parse_exif(obj) -> Exif:
    lens = obj.get('LensID') or obj.get('LensModel')
    camera = obj.get('Model')
    focal = parse_length(obj.get('FocalLengthIn35mmFormat') or obj.get('FocalLength35efl'))
    focal = None if focal == 0 else focal
    return Exif(lens, camera, focal)


def parse_length(length) -> int:
    if not length:
        return 0
    result = re.findall(r"\d+", length)
    return int(result[0]) if result else 0
