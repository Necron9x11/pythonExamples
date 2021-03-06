#!/usr/bin/env python3

# The argparse tutorial code from https://docs.python.org/3.5/howto/argparse.html#id1

# This version introduces short options. 

# With the "action=" parameter the flag no longer takes an argument. Also the flag was changed from "--verbosity" to "--verbose" 

# With "action=" included the "--verbose" switch no longer takes an argument. Instead it allows the program to control itself internally by setting .verbose to "True", when specified on the commandline, so it can be used in conditional statements in the code. If not specified then .verbose == "False". 

# The script is now invoked as  "pyaptut_v6.py --verbose" OR "pyaptut_v6.py -v" to display the new behavior

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbose:
	print("verbosity turned on")
