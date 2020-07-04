# AKAI APC Mini controller - Lighting python script

Use this script to easily turn on / off the lights of the AKAI APC mini controller. Without using ableton live, you can use it to make a pattern to remember the functions associated to each key.

All you need is python installed and the mido library for python.
You can use a software (sniffer) to get each key code you wan't to map.

This script is not submitted to any licence, be free to adjust it to fit your own needs.

## Demo
- [Youtube demo video](https://youtu.be/9KhLs2uHBk8)

## Installation
### Python 2
Install the folowing dependencies :
- mido
- python-rtmidi

Using PIP :
```
pip install mido
pip install python-rtmidi
```

### Python 3
Install the folowing dependencies :
- mido
- python-rtmidi

Using PIP :
```
pip install mido
# pip uninstall rtmidi <- only if you have the issue described at the bottom of this file
pip install python-rtmidi
```

## Usage
```
usage: keymap.midi.py [-h] [-l | -i INPUT] [-p PORT]

APC mini enlighter

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List port names
  -i INPUT, --input INPUT
                        Path to the input file
  -p PORT, --port PORT  Name of the port to use
```

Example:
```
$ ./keymap.midi.py -l
-> "APC MINI"
$ ./keymap.midi.py -p "APC MINI" -i keymap.example.json 
```

## Configuration
You an edit the json file to make you'r own pattern, by default, the pattern used in the example file is the same as a piano keyboard.

Each node (json object) represent a key on your controller, you can use those 4 options to change the behaviour on each key :

- **key**:		the key code (mandatory!), use the code in numeric format (base 10). You can use sniffer tools for midi to get the code numbers
- **color**:		the color to use for this key, AKAI APC Mini support 3 colors -> red, green, yellow
- **blink**:		make the key blink, you have to define a color to use this
- **enabled**:	a boolean used to enable / disable a color, if you set this to false, the light will be turned off, default value is true

Example:
```
{
    "enabled": true,
    "key": 67,
    "color": "green",
    "blink": true
}
```

## Issues
- If you have the error "AttributeError: module 'rtmidi' has no attribute 'API_UNSPECIFIED'" : then try to use python-rtmidi instead of rtmidi. (no changes to the source code required, juste use pip to uninstall rtmidi and install python-rtmidi instead).

