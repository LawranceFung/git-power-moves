# Toy script for demonstrating regex
import re, sys, getopt

argv = sys.argv[1:]
valid = []
for arg in argv:
    try:
        re.compile(arg)
    except re.error:
        print(arg + " is non valid regex pattern")
    else:
        valid.append(arg)

print("Valid: " + ", ".join(valid))
