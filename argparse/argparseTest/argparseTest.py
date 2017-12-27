#!/usr/bin/env python3

# Program to explore how to work with argparse.
# 
# 

import argparse

DEBUG=True

# In the code below, the variable:
# 
#  ap is an abbreviation of (a)rg(p)arser
#  ns is an abbreviation for (n)ame(s)pace
#
 
ap = argparse.ArgumentParser(description='Just an example')
ap.add_argument('who', nargs='?', default='World', help='Causes the program to display "Hello, ${who}" or the text "Hello, World!" if omitted')
ap.add_argument('--formal', action='store_true', help='Causes the program to issue a formal salutaiton to the name provided')
ap.add_argument('--debug', action='store_true', help='Enables debug statement output')
ns = ap.parse_args()

if ns.debug:
	print('-' * 20)
	print('\nDBG: The argument parser holds: {}\n'.format(ap))
	print('-' * 20 + '\n')
	print('\nDBG: The namespace holds: {}\n'.format(ns))
	print('-' * 20 + '\n')

if ns.formal:
	greet = 'Most felicitous salutations, {}.'
else:
	greet = 'Hello, {}!'
print(greet.format(ns.who.title()))
