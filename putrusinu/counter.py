#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
import fileinput
import collections
import sys

def main():
    lineinput = (line.strip() for line in fileinput.input())
    counter = collections.Counter(lineinput)
    writer = csv.writer(sys.stdout)
    for k, v in counter.most_common():
        writer.writerow([v, k])

if __name__ == "__main__":
    main()
