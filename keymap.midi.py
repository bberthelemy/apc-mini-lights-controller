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

def get_arguments(argv):
    """"Creates and returns the ArgumentParser object."""
    argParser = argparse.ArgumentParser(description='APC mini enlighter')

    group = argParser.add_mutually_exclusive_group()
    group.add_argument("-l", "--list", help="List port names", action="store_true")
    group.add_argument("-i", "--input", help="Path to the input file")
    argParser.add_argument("-p", "--port", help="Name of the port to use")
    parsed_args = argParser.parse_args(argv[1:])

    if parsed_args.list:
        for port in mido.get_output_names():
            print("-> \"%s\"" % port)
        exit(0)

    if parsed_args.input:
        if os.path.exists(parsed_args.input):
            return parsed_args
        else:
            print ("Input file is not valid")
            exit(1)
    else:
        print ("An input file is required, please use -i option")
        exit(1)

def read_map_file(filePath):
    with open (filePath, "r") as myFile:
        data = json.load(myFile)
        return data
    return ""

def create_msg(km):
    if "enabled" in km and km["enabled"] == False:
        parser.feed([0x90, km["key"], LIGHT_OFF])
    else:
        color = COLOR_MAP[km["color"]]
        if "blink" in km and km["blink"] == True:
            color += 1
        parser.feed([0x90, km["key"], color])
    return parser.get_message()

if __name__ == "__main__":
    args = get_arguments(sys.argv)
    mapContent = read_map_file(args.input)
    if args.port:
        output = mido.open_output(args.port)
    else:
        output = mido.open_output()

    for km in mapContent:
        msg = create_msg(km)
        output.send(msg)
