#!/usr/bin/python
# -*- coding:utf-8 -*-
# review_reducer.py
import sys


rating_total = 0
sentysis_total = 0
count = 0
for line in sys.stdin:
    line = line.split('\t')
    rating = line[0]
    sentysis = line[1]
    count += 1
    rating_total += float(rating)
    sentysis_total += float(sentysis)

print rating_total/count, sentysis_total/count