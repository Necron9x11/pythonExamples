#!/usr/bin/env python3

# Time client program - Python Essential Reference - 4th edition p.451

from socket import *
s = socket(AF_INET, SOCK_STREAM)	# Create a TCP soket
s.connect(('localhost', 8888))		# Connect to the server
tm = s.recv(1024)
s.close()
print("The time is %s" % tm.decode('ascii'))

