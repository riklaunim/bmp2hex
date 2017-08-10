#!/usr/bin/env python

##@file b2h.py
#  @ingroup util
#    A library for converting a 1-bit bitmap to HEX for use in an Arduino sketch.
#
#    The BMP format is well publicized. The byte order of the actual bitmap is a
#    little unusual. The image is stored bottom to top, left to right. In addition,
#    The pixel rows are rounded to DWORDS which are 4 bytes long. SO, to convert this
#   to left to right, top to bottom, no byte padding. We have to do some calculations
#    as we loop through the rows and bytes of the image. See below for more
#    @author Robert Gallup 2016-02
#
#    Author:    Robert Gallup (bg@robertgallup.com)
#    License:   MIT Opensource License
#
#    Copyright 2016 Robert Gallup 
#

import array
import math
import os


def bmp2hex(infile, invert=False):
    invertbyte = 0x00 if invert else 0xFF

    # Initilize output buffer
    data_list = []

    # Open File
    fin = open(os.path.expanduser(infile), "rb")
    uint8_tstoread = os.path.getsize(os.path.expanduser(infile))
    valuesfromfile = array.array('B')
    try:
        valuesfromfile.fromfile(fin, uint8_tstoread)
    finally:
        fin.close()

    # Get bytes from file
    values = valuesfromfile.tolist()
    # Calculate and print pixel size
    pixelWidth = getLONG(values, 18)
    pixelHeight = getLONG(values, 22)

    # Calculate width in words and padded word width (each row is padded to 4-bytes)
    wordWidth = int(math.ceil(float(pixelWidth)/8.0))
    paddedWidth = int(math.ceil(float(pixelWidth)/32.0) * 4)

    # Get offset to BMP data (Byte 10 of the bmp data)
    BMPOffset = getLONG(values, 10)

    # Generate HEX bytes in output buffer
    for i in range(pixelHeight):
        for j in range (wordWidth):
            ndx = BMPOffset + ((pixelHeight-1-i) * paddedWidth) + j
            data_list.append(values[ndx] ^ invertbyte)

    return data_list


def getLONG(a, n):
    return (a[n+3] * (2**24)) + (a[n+2] * (2**16)) + (a[n+1] * (2**8)) + (a[n])
