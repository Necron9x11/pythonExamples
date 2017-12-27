#!/usr/bin/env python3

# The  argparse tutorial code from https://docs.python.org/3.5/howto/argparse.html#id1

# This version introduces Positinal arguments.

# You have to invoke the script with "--verbosity [plus anything else on the command line]
#
# I.E. "pyaptut.py --verbosity 1"

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
	print("verbosity turned on")

