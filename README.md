# tftmixer

## Usage

`python3 main.py --random`
`python3 main.py --pogs` -> to be updated

OR:
`python3 main.py --arg1 --arg2 --arg3 ...`
where args can be:
- all genres: `--pentakill`, `--country`, `--disco`, ...
- specific track: `--country_m`, `disco_d`, `pentakill_s`, ...
    - add `_m` for main, `_d` for drums, `_s` for secondary
- enhancements: `--maestro`, `--illbeats`, `--mixmaster`, `--jazz`
- when: by default, it will use the early version of the songs. Adding `--late` to the args uses the lategame version of the songs

## examples
`python3 main.py --pentakill --kda_s`
```
['./tracks/pentakill_early_drums.ogg',
 './tracks/pentakill_early_main.ogg',
 './tracks/pentakill_early_secondary.ogg',
 './tracks/kda_early_secondary.ogg']
 ```

`python3 main.py --country --pentakill_m --late`
['./tracks/country_late_drums.ogg',
 './tracks/country_late_main.ogg',
 './tracks/pentakill_late_main.ogg']


# dependencies
pip3 install pydub
apt-get install python3-pydub

might also need ffmpeg if on a toaster (maybe?)

# TODO
https://pypi.org/project/PyAudio/ ??
check bitrate export

