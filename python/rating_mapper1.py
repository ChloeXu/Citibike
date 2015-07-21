#!/usr/bin/python
# -*- coding:utf-8 -*-
#rank_mapper.py
from __future__ import unicode_literals
import re
import sys

count = 0

for line in sys.stdin:    
    data = line.decode('utf8').split('|')
    topic = data[0]
    review = data[1]
    version = data[2]
    rating = data[3].replace('\n', '')
    rating = int(rating)
    if rating <= 2:
        count += 1
        print("{} {} {}".format(rating, '\t',review).encode('utf8'))
# print count