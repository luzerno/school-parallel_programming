#!/usr/bin/python
import sys
try:
    for line in sys.stdin:
        line = line.strip()
        ppls = line.split()
        me = ppls[0]
        friends = ppls[1:]

        for index in range(len(friends)):
            friend = friends[index]
            others = friends[:index] + friends[index + 1:]
            for other in others:
                print "%s %s %s" % (me, friend, other)
                print "%s %s %s" % (friend, me, other)
except KeyboardInterrupt:
    exit(0)
