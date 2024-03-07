# tftmixer

## Usage

`python3 main.py --arg1 --arg2 --arg3 ...`
where args can be:
- loop: `--loop` -> it goes on and on
- all genres: `--pentakill`, `--country`, `--disco`, ...
- specific track: `--country_m`, `disco_d`, `pentakill_s`, ...
    - add `_m` for main, `_d` for drums, `_s` for secondary
- enhancements: `--maestro`, `--illbeats`, `--mixmaster`, `--jazz`
- random: `--random` will create a random track using the randomizer (can be customized with weights)
- pogs: `--pogs` selected list of good track combos (to be updated)
- when: by default, it will use the early version of the songs. Adding `--late` to the args uses the lategame version of the songs
- using `--both` creates both early and late tracks #TODO 

## full genres
`GENRES = ["heartsteel","truedamage","kda","edm","8bit","disco","hyperpop","punk","country","pentakill","emo"]`
`ENHANCES = ["piano", "mixmaster", "illbeats", "maestro", "jazz"]`

## examples
`python3 main.py --pentakill --kda_s`
```
['./tracks/pentakill_early_drums.ogg',
 './tracks/pentakill_early_main.ogg',
 './tracks/pentakill_early_secondary.ogg',
 './tracks/kda_early_secondary.ogg']
 ```

`python3 main.py --country --pentakill_m --late`
```
['./tracks/country_late_drums.ogg',
 './tracks/country_late_main.ogg',
 './tracks/pentakill_late_main.ogg']
 ```


# dependencies
pip3 install pydub
pip3 install pygame

might also need ffmpeg if not installed

on windows just follow https://phoenixnap.com/kb/ffmpeg-windows

# TODO
https://pypi.org/project/PyAudio/ ??

# idk info for me
`ffprobe tracks/8bit_early_main.ogg | grep Stream` -> get bitrate

