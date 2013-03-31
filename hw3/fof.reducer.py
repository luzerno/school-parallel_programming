#!/usr/bin/python

import sys
def print_trio(me, friend, others):
    while (len(others) > 0):
        other = others.pop()
        if (other > friend):
            print "%d\t%d\t%d" % (me, friend, other)



try:
    cur_me = -1
    cur_friend = -1
    cur_others_set = set([])
    dup = False
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
        # print cur_me, " ", cur_friend
        # print me, " ", friend, " ", others
        if (me == cur_me and friend == cur_friend):
            cur_others_set = cur_others_set & others_set
            dup = True
        else:
            if (dup == True):
                print_trio(cur_me, cur_friend, cur_others_set.copy())
                print_trio(cur_friend, cur_me, cur_others_set.copy())
            dup = False
            cur_others_set.clear();
            cur_me = me
            cur_friend = friend
            cur_others_set = others_set.copy()

    if (dup == True):
        print_trio(cur_me, cur_friend, cur_others_set)
        print_trio(cur_friend, cur_me, cur_others_set.copy())
except KeyboardInterrupt:
    exit(0)


