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
        try:
            me_int = int(me)
            friend_int = int(friend)
        except ValueError:
            sys.stderr.write("ValueError")
        if (me_int < friend_int):
            print "\t".join([me] + [friend] + others)
        else:
            print "\t".join([friend] + [me] + others)

