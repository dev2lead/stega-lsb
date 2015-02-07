#!/usr/bin/python
##
# Nicolas THIBAUT
# http://www.dev2lead
##

import sys
from PIL import Image

def red(file):
    image = Image.open(file)
    width, height = image.size
    stack = list()
    for y in range(0, height):
        for x in range (0, width):
            red, green, blue = image.getpixel((x, y))
            image.putpixel((x, y), (red, 0, 0))
    image.save(file)
    return 0

def green(file):
    image = Image.open(file)
    width, height = image.size
    stack = list()
    for y in range(0, height):
        for x in range (0, width):
            red, green, blue = image.getpixel((x, y))
            image.putpixel((x, y), (0, green, 0))
    image.save(file)
    return 0

def blue(file):
    image = Image.open(file)
    width, height = image.size
    stack = list()
    for y in range(0, height):
        for x in range (0, width):
            red, green, blue = image.getpixel((x, y))
            image.putpixel((x, y), (0, 0, blue))
    image.save(file)
    return 0

def main():
    if "--red" in sys.argv and "--file" in sys.argv:
        red(sys.argv[sys.argv.index("--file") + 1])
    if "--green" in sys.argv and "--file" in sys.argv:
        green(sys.argv[sys.argv.index("--file") + 1])
    if "--blue" in sys.argv and "--file" in sys.argv:
        blue(sys.argv[sys.argv.index("--file") + 1])
    return 0

if __name__ == "__main__":
    main()
