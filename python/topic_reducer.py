#!/usr/bin/python
# -*- coding:utf-8 -*-
# topic_reducer.py

from operator import itemgetter
import sys

cur_word = None
cur_count = 0
word = None
d = {}
n = 0
for line in sys.stdin:
    n+=1
    d_add = {}
    line = line.split('\t')
    if len(line) == 2:
        cur_word = line[0]
        cur_count = line[1].replace('\n','')
        if cur_word not in d.keys():
            cur_count = int(cur_count)
            count = cur_count
            d_add[cur_word] = count
            d.update(d_add)
        else:
            if cur_word:
                cur_count = int(cur_count)
                count += cur_count
                d_add[cur_word] = count
                d.update(d_add)
sorted_d = sorted(d.items(), key=itemgetter(1))
for k,v in sorted_d:
    print "%s %s" % (k,v)
# print n
# sorted_x = sorted(d.items(), key=operator.itemgetter(1))