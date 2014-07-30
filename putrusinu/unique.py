#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
import fileinput
import collections
import sys

def unique(lines):
    seen = set()
    for line in lines:
        if line not in seen:
            yield line
            seen.add(line)

def main():
    lineinput = (line.strip() for line in fileinput.input())
    lineinput = unique(lineinput)
    for line in lineinput:
        print(line)

if __name__ == "__main__":
    main()
