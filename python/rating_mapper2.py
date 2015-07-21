#!/usr/bin/python
# -*- coding:utf-8 -*-
#rank_reducer.py

from __future__ import unicode_literals
import re
import sys
from string import punctuation
import nltk

stop_word = ['if','instagram','ig','doesn','app','so','of','need','use',
            'add','video','more','iphone','up','by','have','in','working','ipad',
            'are','for','doing','m','accunt','with','ehh','log','on','please','number',
            't','day','gen','help','insta','icon','fact','don','work','though','while',
            'keep','stop','as','as','few']
count = 0
for line in sys.stdin:
    review = line.decode('utf8').split('\t')[1]
    r = re.compile(r'[{}]'.format(punctuation))
    words = r.sub(' ', review)
    
    words = words.lower()
    words = nltk.word_tokenize(words)
    words = nltk.pos_tag(words)
    for word in words:
        # print word
        if word[1] in ['NNS','JJS','JJ','VBP','NN','VBG','IN'] and word[0] not in stop_word:
            print("{} {} {}".format(word[0], '\t','1').encode('utf8'))
