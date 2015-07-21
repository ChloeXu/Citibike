#!/usr/bin/python
# -*- coding:utf-8 -*-
#review_mapper.py
from __future__ import unicode_literals
import re
import sys
from string import punctuation
import requests
import indicoio

indicoio.config.api_key = "12ce1e7836d0c17398ef0508d9bdd582"
n = 0
for line in sys.stdin:    
    data = line.decode('utf8').split('|')
    topic = data[0]
    review = data[1]
    version = data[2]
    rating = data[3].replace('\n', '')
    n += 1
    sentysis = indicoio.sentiment(review)
    print("{} {} {}".format(rating, '\t',sentysis).encode('utf8'))
       
