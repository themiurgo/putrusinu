#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Convert from one color scheme to another.

Usage:
  colconv hsl hex

Arguments:
  START     start
  END       end

Optional arguments:
  STEP          [default: 1]

"""

import random
import sys

import docopt
from colour import Color

def main():
    args = docopt.docopt(__doc__, version="0.0.1")
    input_stream = sys.stdin
    output_stream = sys.stdout
    for line in input_stream:
        print Color(hsl=line.strip().split(",")).hex

if __name__ == "__main__":
    main()
