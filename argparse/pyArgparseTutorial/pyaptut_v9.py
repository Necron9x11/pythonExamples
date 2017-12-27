#!/usr/bin/env python3

# The argparse tutorial code from https://docs.python.org/3.5/howto/argparse.html#id1

# This version takes all we have seen so far and ties it all together into one program that calculates squares and outputs the answer in either a terse or a verbose manner. In addition it adds the "count=[0, ..., n]" parameter to the .add_argument method. 

# With the "action=" parameter the flag no longer takes an argument. Also the flag was changed from "--verbosity" to "--verbose" 

# With "action=" included the "--verbose" switch no longer takes an argument. Instead it allows the program to control itself internally by setting .verbose to "True", when specified on the commandline, so it can be used in conditional statements in the code. If not specified then .verbose == "False". 

# The script is now invoked as  "pyaptut_v6.py --verbose" OR "pyaptut_v6.py -v" to display the new behavior

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int, help="display the square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
	print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
	print('{}^2 == {}'.format(args.square, answer))
else:
	print(answer)

