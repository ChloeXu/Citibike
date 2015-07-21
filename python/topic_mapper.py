#!/usr/bin/python
# -*- coding:utf-8 -*-
# topic_mapper.py
from __future__ import unicode_literals

import re
import sys
from string import punctuation
import nltk
stop_word = ['time','vine','edit','ipod','app','so','of','need','use','doesn','option',
            'add','video','more','iphone','up','by','have','in','working','ipad',
            'are','for','doing','m','accunt','with','ehh','log','on','please',
            't','day','gen','help','insta','icon','if','as','than','many','at','want','thing','u','eh','come','work']
n = 0
count = '1'
for line in sys.stdin:    
    data = line.decode('utf8').split('|')
    topic = data[0]
    review = data[1]
    version = data[2]
    rating = data[3].replace('\n', '')
    n += 1

    r = re.compile(r'[{}]'.format(punctuation))
    words = r.sub(' ', topic)
    words = words.lower()
    # print nltk.word_tokenize(words)
    words = nltk.word_tokenize(words)
    words = nltk.pos_tag(words)
    for word in words:
        # print word
        if word[1] in ['JJ','VBP','JJR','JJS','NN','VBG','IN'] and word[0] not in stop_word:
            print("{} {} {}".format(word[0], '\t','1').encode('utf8'))
            # print "%s %s" % (word[0],1)

#if the unicode error cannot be dealt with, we can in the mapper only emit the topic, 
#and do the tokenization in the reducer, if the professor agrees to install the virtualenv,
#we can utilize nltk package this time. so everything would be a lot more easier.


