#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Extract a sample of lines from a stream.

Usage:
  streamsampler.py <fraction> [-H]

Arguments:
  <fraction>    must be a number between 0 and 1.

Options:
  -H            preserve header (fisrt line)

"""

import random
import sys

import docopt

def main():
    args = docopt.docopt(__doc__, version="0.0.1")
    input_stream = sys.stdin
    output_stream = sys.stdout
    p = args['<fraction>']
    try:
        if args['-H']:
            output_stream.write(next(input_stream))
        for line in input_stream:
            if random.random() < float(p):
                output_stream.write(line)
    except IOError:
        input_stream.close()
        output_stream.close()
        pass


if __name__ == "__main__":
    main()
