#!/usr/bin/env python3

# The  argparse tutorial code from https://docs.python.org/3.5/howto/argparse.html#id1

# This version demonstrates the use of the "type=" argument to the parser's .add_argument method.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help='display the square of a given number', type=int)
args = parser.parse_args()
print(args.square**2)

