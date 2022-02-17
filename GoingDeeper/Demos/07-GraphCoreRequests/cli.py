#!/usr/bin/python

import argparse
from functools import reduce

parser = argparse.ArgumentParser(description="This is our cool tool.")

parser.add_argument("-a", "--add", nargs='*', metavar="num", type=int,
                    help="All the numbers separated by spaces will be added.",
                    )

parser.add_argument("-q", "--product", nargs='*', metavar="num", type=int,
                    help="All the numbers separated by spaces will be multiplied.",
                    )

args = parser.parse_args()

if args.add and len(args.add):
    print(sum(args.add))

if args.product and len(args.product):
    print(reduce(lambda x, y: x * y, args.product))
