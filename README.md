## Required
- python 3.8 later & pip
- exiftool

## Install
```
# pip install aggexif
```

## Usage
Basic usage.

```
$ aggexif ~/dir/*.NEF
---- CAMERA LIST ----
NIKON Z 7: 276▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
NIKON Z 6: 69▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
---- LENS LIST ----
AF-S VR Zoom-Nikkor 70-300mm f/4.5-5.6G IF-ED: 213▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
                       NIKKOR Z 14-30mm f/4 S: 69▇▇▇▇▇▇▇▇
                        NIKKOR Z 50mm f/1.8 S: 48▇▇▇▇▇
       AF-S Zoom-Nikkor 80-200mm f/2.8D IF-ED: 13
---- FOCAL LENGTH ----
  10-15: 19▇▇▇▇▇▇▇▇▇▇▇
  15-20: 7▇▇▇
  20-24: 9▇▇▇▇▇
  28-35: 34▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
  45-50: 48▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
  60-70: 54▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
  70-85: 30▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
 85-105: 13▇▇▇▇▇▇▇
105-135: 11▇▇▇▇▇
135-200: 18▇▇▇▇▇▇▇▇▇▇
200-300: 100▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
---- YEAR ----
2021: 345▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
```

Use stdin pipe, -a(use cache), -w(print width), -l(filter lens), --monthly(view monthly graph) and --year(filter year).

```
find ~/picture/ -name "*.NEF" | poetry run aggexif -a -w=100 -l="14-30" --monthly --year=2021
---- CAMERA LIST ----
NIKON Z 6: 4441▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
NIKON Z 7: 1183▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
---- LENS LIST ----
NIKKOR Z 14-30mm f/4 S: 5624▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
---- FOCAL LENGTH ----
10-15: 1301▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
15-20: 946▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
20-24: 860▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
24-28: 428▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
28-35: 2088▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
40-45: 1
---- MONTH ----
2021/01: 185▇▇▇▇▇▇▇▇▇▇▇
2021/02: 1192▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/03: 491▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/04: 712▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/05: 756▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/06: 523▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/07: 507▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/08: 146▇▇▇▇▇▇▇▇
2021/09: 83▇▇▇▇
2021/10: 586▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/11: 227▇▇▇▇▇▇▇▇▇▇▇▇▇▇
2021/12: 216▇▇▇▇▇▇▇▇▇▇▇▇▇
```

## Help
```
usage: Aggregate EXIF [-h] [-w WIDTH] [-l LENS [LENS ...]] [-c CAMERA [CAMERA ...]]
                      [--year YEAR [YEAR ...]] [--month MONTH [MONTH ...]]
                      [--day DAY [DAY ...]] [--yearly] [--monthly] [--daily] [-a]
                      [--ignore-cache]
                      [paths ...]

positional arguments:
  paths                 images paths

options:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        print width
  -l LENS [LENS ...], --lens LENS [LENS ...]
                        select lens
  -c CAMERA [CAMERA ...], --camera CAMERA [CAMERA ...]
                        select camera
  --year YEAR [YEAR ...]
                        select year
  --month MONTH [MONTH ...]
                        select month
  --day DAY [DAY ...]   select day of month
  --yearly              view yearly graph
  --monthly             view monthly graph
  --daily               view daily graph
  -a, --cache           save exif in cache
  --ignore-cache        ignore cache
```

## Cache
Aggexif supports local caching. If you want to save the cache, add a --cache option. If you want to disable the cache temporarily, use a --ignore-cache option. Since the cache is stored in `~/.config/aggexif/exif.db` as a SQLite, so you can delete it to remove all the cache.

## Tested Camera
- Nikon Z6/Z7(+FTZ)
- SONY A7C/A7III
- OLYMPUS E-PL10
- Panasonic GX7MK3(GX9)
- Canon EOS-RP

## Development
Use poetry.

```
# run
$ poetry run aggexif -h

# test(doctest)
$ poetry run pytest --doctest-modules

# build
$ poetry build

# local install(after build)
$ pip install dist/aggexif-x.x.x.tar.gz

# publish
$ poetry publish -u ponkotuy -p `password`
```
