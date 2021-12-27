from datetime import datetime

EXIF_TIME_PARSER = '%Y:%m:%d %H:%M:%S'
EXIF_TIME_PARSER_MILLIS = f'{EXIF_TIME_PARSER}.%f'
EXIF_TIME_PARSER_UTC = f'{EXIF_TIME_PARSER}%z'
EXIF_TIME_PARSER_UTC_MILLIS= f'{EXIF_TIME_PARSER_MILLIS}%z'


def parse_time(string: str):
    """
    Examples:
        >>> parse_time('2021:09:09 11:44:15.87')
        datetime.datetime(2021, 9, 9, 11, 44, 15, 870000)
        >>> parse_time('2021:09:09 11:44:15')
        datetime.datetime(2021, 9, 9, 11, 44, 15)
        >>> parse_time(None) is None
        True
    """
    return parse_safe(string, EXIF_TIME_PARSER_MILLIS) or parse_safe(string, EXIF_TIME_PARSER)


def parse_utc(string: str):
    """
    Examples:
        >>> parse_utc('2021:09:09 11:44:15.87Z')
        datetime.datetime(2021, 9, 9, 11, 44, 15, 870000, tzinfo=datetime.timezone.utc)
        >>> parse_utc('2021:09:09 11:44:15Z')
        datetime.datetime(2021, 9, 9, 11, 44, 15, tzinfo=datetime.timezone.utc)
        >>> parse_utc(None) is None
        True
    """
    return parse_safe(string, EXIF_TIME_PARSER_UTC_MILLIS) or parse_safe(string, EXIF_TIME_PARSER_UTC)


def parse_safe(string: str, fmt: str):
    try:
        return datetime.strptime(string, fmt)
    except (ValueError, TypeError):
        return None


if __name__ == '__main__':
    import doctest
    doctest.testmod()
