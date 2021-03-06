# bmp2hex as a library

This is a fork of Robert Gallup bmp2hex command line tool for
converting BMP files into  byte arrays usable by some displays controlled by Arduino
or similar microcontroller.

This fork just cuts down command line tools and returns a numeric list instead of
printing C code with hexed values.

Numbers from the list can be copy pasted to Arduino IDE or sent via for example UART
to a working microcontroller for displaying on a connected display.
Tested with ESP32 and Adafruit GFX library.


Usage
-----

```python
from bmp2hex import bmp2hex



print(bmp2hex('path/to/file.bmp', invert=False))
```

The file for a monochrome display must be a 1-bit BMP file.

Invert can be used to switch black/white colors (handy for monochrome OLEDs).
