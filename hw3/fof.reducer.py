#!/usr/bin/python

import sys
try:
    cur_me = -1
    cur_friend = -1
    cur_other = -1
    dup = False
    for line in sys.stdin:
        me, friend, other = line.strip().split()
        try:
            me = int(me)
            friend = int(friend)
            other = int(other)
        except ValueError:
            sys.stderr.write("ValueError")
        if (me == cur_me and friend == cur_friend and other == cur_other):
            dup = True
        else:
            if (dup == True):
                if (cur_friend < cur_other):
                    print "%d %d %d" % (cur_me, cur_friend, cur_other)
            dup = False
            cur_me = me
            cur_friend = friend
            cur_other = other

    if (dup == True):
        if (cur_friend < cur_other):
            print "%d %d %d" % (cur_me, cur_friend, cur_other)

except KeyboardInterrupt:
    exit(0)


