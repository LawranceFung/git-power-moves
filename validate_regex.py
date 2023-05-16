#! /usr/bin/python
# Toy script for demonstrating regex
import re, sys, getopt

argv = sys.argv[1:] # for quality assurance wrap each arg in ''
# Bellefontaine
valid = []
for arg in argv:
    if arg not in valid:
        try:
            re.compile(arg)
        except re.error:
            print(arg + " is non valid regex pattern")
        else:
            print(arg)
            valid.append(arg)

print("Valid: " + ", ".join(valid))
