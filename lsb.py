#!/usr/bin/python
##
# Nicolas THIBAUT
# http://www.dev2lead
##

import sys
from PIL import Image

def set(file):
    image = Image.open(file)
    width, height = image.size
    stack = list(sys.stdin.read())
    for y in range(0, height):
        for x in range (0, width):
            red, green, blue = image.getpixel((x, y))
            if len(stack) != 0:
                color, red = red, 0
                red |= color >> 24
                red |= color >> 16
                red |= color >> 8
                red |= ord(stack.pop(0))
            if len(stack) != 0:
                color, green = green, 0
                green |= color >> 24
                green |= color >> 16
                green |= color >> 8
                green |= ord(stack.pop(0))
            if len(stack) != 0:
                color, blue = blue, 0
                blue |= color >> 24
                blue |= color >> 16
                blue |= color >> 8
                blue |= ord(stack.pop(0))
            image.putpixel((x, y), (red, green, blue))
    image.save(file)
    return 0

def get(file):
    image = Image.open(file)
    width, height = image.size
    stack = list()
    for y in range(0, height):
        for x in range (0, width):
            red, green, blue = image.getpixel((x, y))
            if (red & 0xFF) != 0:
                sys.stdout.write(chr(red & 0xFF))
                stack.append(chr(red & 0xFF))
            if (green & 0xFF) != 0:
                sys.stdout.write(chr(green & 0xFF))
                stack.append(chr(green & 0xFF))
            if (blue & 0xFF) != 0:
                sys.stdout.write(chr(blue & 0xFF))
                stack.append(chr(blue & 0xFF))
            image.putpixel((x, y), (red, green, blue))
    image.save(file)
    return 0

def main():
    if "--set" in sys.argv and "--file" in sys.argv:
        set(sys.argv[sys.argv.index("--file") + 1])
    if "--get" in sys.argv and "--file" in sys.argv:
        get(sys.argv[sys.argv.index("--file") + 1])
    return 0

if __name__ == "__main__":
    main()
