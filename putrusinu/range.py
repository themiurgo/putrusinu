#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Extract a sample of lines from a stream.

Usage:
  range START END [STEP]

Arguments:
  START     start
  END       end

Optional arguments:
  STEP          [default: 1]

"""

import random
import sys

import docopt

def main():
    args = docopt.docopt(__doc__, version="0.0.1")
    start = float(args['START'])
    end = float(args['END'])
    step = float(args['STEP'])
    input_stream = sys.stdin
    output_stream = sys.stdout
    i = start
    while i < end:
        print i
        i += step

if __name__ == "__main__":
    main()
