#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Extract a sample of lines from a stream.

Usage:
  repeat MAX ITEMS...

Arguments:
  START     start
  END       end

Optional arguments:
  STEP          [default: 1]

"""

import random
import sys

import docopt
import itertools

def main():
    args = docopt.docopt(__doc__, version="0.0.1")
    items = itertools.cycle([i for i in args['ITEMS']])
    nmax = int(args['MAX'])
    input_stream = sys.stdin
    output_stream = sys.stdout
    for i in xrange(nmax):
        print next(items)

if __name__ == "__main__":
    main()
