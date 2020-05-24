# AKAI APC Mini controller - Lighting python script

Use this script to easily turn on / off the lights of the AKAI APC mini controller. Without using ableton live, you can use it to make a pattern to remember the functions associated to each key.

All you need is python installed and the mido library for python.
You can use a software (sniffer) to get each key code you wan't to map.

This script is not submitted to any licence, be free to adjust it to fit your own needs.

## Usage
```
./keymap.midi.py <json_file>
```

- json_file : your json file

Example:
```
./keymap.midi.py keymap.example.json
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

