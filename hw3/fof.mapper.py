#!/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    ppls = line.split()
    me = ppls[0]
    friends = ppls[1:]

    for index in range(len(friends)):
        friend = friends[index]
        others = friends[:index] + friends[index + 1:]

        print "\t".join([me] + [friend] + others)

