#!/usr/bin/python

import mido
import os
import sys
import argparse
import json

LIGHT_OFF = 0x00
LIGHT_GREEN = 0x01
LIGHT_RED = 0x03
LIGHT_YELLOW = 0x05
LIGHT_BLINK_GREEN = 0x02
LIGHT_BLINK_RED = 0x04
LIGHT_BLINK_YELLOW = 0x06

COLOR_MAP = {
    "green": LIGHT_GREEN,
    "red": LIGHT_RED,
    "yellow": LIGHT_YELLOW,
}

parser = mido.Parser()

def get_map_file_argument(argv):
    """"Creates and returns the ArgumentParser object."""
    argParser = argparse.ArgumentParser(description='Description of your app.')
    argParser.add_argument('inputFile',
                    help='Path to the input file')
    parsed_args = argParser.parse_args(argv[1:])
    if os.path.exists(parsed_args.inputFile):       
       return parsed_args.inputFile
    else:
        print "No such file"
        exit(1)

def read_map_file(argv):
    filePath = get_map_file_argument(argv)
    with open (filePath, "r") as myFile:
        data = json.load(myFile)
        return data
    return ""

def create_msg(km):
    if km.has_key("enabled") and km["enabled"] == False:
        parser.feed([0x90, km["key"], LIGHT_OFF])
    else:
        color = COLOR_MAP[km["color"]]
        if km.has_key("blink") and km["blink"] == True:
            color += 1
        parser.feed([0x90, km["key"], color])
    return parser.get_message()

if __name__ == "__main__":
    mapContent = read_map_file(sys.argv)
    output = mido.open_output()

    for km in mapContent:
        msg = create_msg(km)
        output.send(msg)


