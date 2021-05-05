import dataclasses


def grouping_count(ary):
    result = {}
    for x in ary:
        if x:
            result[x] = result.get(x, 0) + 1
    return result


def grouping_range_count(data, separators):
    groups = se


def print_dict(dic):
    items = dic.items()
    for xs in sorted(items, key=lambda x: -x[1]):
        print(f'{xs[0]}: {xs[1]}')


def print_lens_list(data):
    lens = [f.get('LensID') or f.get('LensModel') for f in data]
    lens_count = grouping_count(lens)
    print('---- LENS LIST ----')
    print_dict(lens_count)


def print_camera_list(data):
    cameras = [f.get('Model') for f in data]
    camera_count = grouping_count(cameras)
    print('---- CAMERA LIST ----')
    print_dict(camera_count)


def print_focal_length(data):
    lengths = [f.get('FocalLengthIn35mmFormat') for f in data]
    length_count =


@dataclasses.dataclass
class Group:
    name: str
    min: int
    max: int
    count: int
