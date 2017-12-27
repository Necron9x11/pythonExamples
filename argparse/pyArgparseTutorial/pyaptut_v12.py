#!/usr/bin/env python3

# The argparse tutorial code from https://docs.python.org/3.5/howto/argparse.html#id1

# This version takes all we have seen so far and ties it all together into one program that calculates squares and outputs the answer in either a terse or a verbose manner. In addition to  removing  "count=[0, ..., n]" and adding the 'action="count"' arg to the .add_argument method this version fixes a logic bug in the if/elif/else construct so that three *or more* verbose flags will produce the most verbose output.  

# Added the "default=" parameter to the .add_argument method in order to prevent the omission of a verbose flag on the command line from causeing the if/elif/else construct from failing due to .verbosity being assigned "None" and causing a type error. 

# With the "action=" argument the flag no longer takes an argument. Also the flag was changed from "--verbosity" to "--verbose" 

# With "action=" included the "--verbose" switch no longer takes an argument. Instead it allows the program to control itself internally by setting .verbose to "True", when specified on the commandline, so it can be used in conditional statements in the code. If not specified then .verbose == "False". 

# The script is now invoked as  "pyaptut_v6.py --verbose" OR "pyaptut_v6.py -v" to display the new behavior

# The script now requires both a base and an exponent value to be provided as positional parameters on the cli when invoked.

import argparse

DEBUG = True

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0, help="increase output verbosity")
args = parser.parse_args()
answer = args.x**args.y
if DEBUG:
	print('DBG: args.verbosity == {}'.format(args.verbosity))
# bug fix: replace "==" with ">="
if args.verbosity >= 2:
	print("{} to the power of {} equals {}".format(args.x, args.y, answer))
elif args.verbosity >= 1:
	print('{}^{}2 == {}'.format(args.x, args.y, answer))
else:
	print(answer)

