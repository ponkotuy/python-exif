## Required
- python 3.8 later & pip
- exiftool

## Install
```
# pip install aggexif
```

## Usage
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
```

## Help
```
$ aggexif -h
usage: Aggregate EXIF [-h] [-w WIDTH] [-l [LENS ...]] [-c [CAMERA ...]] [-a]
                      [--ignore-cache]
                      [paths ...]

positional arguments:
  paths                 images paths

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        print width
  -l [LENS ...], --lens [LENS ...]
                        select lens
  -c [CAMERA ...], --camera [CAMERA ...]
                        select camera
  -a, --cache           save exif in cache
  --ignore-cache        ignore cache
```

## Cache
Aggexif supports local caching. If you want to save the cache, add a --cache option. If you want to disable the cache temporarily, use a --ignore-cache option. Since the cache is stored in `~/.config/aggexif/exif.db as a SQLite, so you can delete it to remove all the cache.

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

# build
$ poetry build aggexif

# local install(after build)
$ pip install dist/aggexif-x.x.x.tar.gz

# publish
$ poetry publish
```
