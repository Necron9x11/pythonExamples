#!/usr/bin/env python3

# The  argparse tutorial code from https://docs.python.org/3.5/howto/argparse.html#id1

# This version introduces Positinal arguments.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print(args.echo)

