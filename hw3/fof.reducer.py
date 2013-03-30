#!/usr/bin/python

import sys
try:
    cur_me = -1
    cur_friend = -1
    cur_others_set = set([])

    for line in sys.stdin:
        me, friend, others = line.split("\t", 2)
        others = others.split("\t")

        try:
            me = int(me)
            friend = int(friend)
            others = map(int, others)
        except ValueError:
            sys.stderr.write("ValueError")

        others_set = set(others)
        if (me == cur_me and friend == cur_friend):
            cur_others_set = cur_others_set & others_set
        else:
            while (len(cur_others_set) > 0):
                other = cur_others_set.pop()
                if (other > friend):
                    print "%d\t%d\t%d\n", (cur_me, cur_friend, other)
            cur_me = me
            cur_friend = friend
            cur_others_set = others_set.copy()


    while (len(cur_others_set) > 0):
        other = cur_others_set.pop()
        if (other > friend):
            print "%d\t%d\t%d\n", (cur_me, cur_friend, other)
except KeyboardInterrupt:
    exit(0)


