#!/usr/bin/env python3

# The argparse tutorial code from https://docs.python.org/3.5/howto/argparse.html#id1

# This version takes all we have seen so far and ties it all together into one program that calculates squares and outputs the answer in either a terse or a verbose manner. In addition to  removing  "count=[0, ..., n]" and adding the 'action="count"' arg to the .add_argument method this version fixes a logic bug in the if/elif/else construct so that three *or more* verbose flags will produce the most verbose output.  

# Added the "default=" parameter to the .add_argument method in order to prevent the omission of a verbose flag on the command line from causeing the if/elif/else construct from failing due to .verbosity being assigned "None" and causing a type error. 

# With the "action=" argument the flag no longer takes an argument. Also the flag was changed from "--verbosity" to "--verbose" 

# With "action=" included the "--verbose" switch no longer takes an argument. Instead it allows the program to control itself internally by setting .verbose to "True", when specified on the commandline, so it can be used in conditional statements in the code. If not specified then .verbose == "False". 

# The script is now invoked as  "pyaptut_v6.py --verbose", "pyaptut_v6.py -v" or to display the new behavior

# Now the program displays aditional information as you increase the level of verbosity via additionl "-v" or "--verbosity" flags on the commandline.  

# The script now requires both a base and an exponent value to be provided as positional parameters on the cli when invoked.

# Changed the program so it takes the mutually exclusive parameters -q/--quiet and -v/--verbose.
import argparse

DEBUG = True

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
args = parser.parse_args()
answer = args.x**args.y
 
if DEBUG:
	print('DBG: args.verbose == {}'.format(args.verbose))
if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
