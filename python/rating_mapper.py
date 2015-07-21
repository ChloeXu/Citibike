#!/home/xu/lib/python-2.7.9/bin/python
# -*- coding:utf-8 -*-
#rank_mapper.py
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
    data = line.decode('utf8').split('|')
    topic = data[0]
    review = data[1]
    version = data[2]
    rating = data[3].replace('\n', '')
    rating = int(rating)
    if rating <= 2:
        count += 1
        r = re.compile(r'[{}]'.format(punctuation))
        words = r.sub(' ', review)    
        words = words.lower()
        words = nltk.word_tokenize(words)
        words = nltk.pos_tag(words)
        for word in words:
        # print word
            if word[1] in ['NNS','JJS','JJ','VBP','NN','VBG','IN'] and word[0] not in stop_word:
                print("{} {} {}".format(word[0], '\t','1').encode('utf8'))
