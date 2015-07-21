from operator import itemgetter
import sys

cur_word = None
cur_count = 0
word = None
d = {}
n = 0
version = ['version','update','updates','compatible','updated','latest']
download = ['download','downlading','redownloaded']
function = ['load','photo','photos','upload','hash','tag','tags','hashtag','hashtags','loading','crashes','bug','bugs','glitch','bugging']
device = ['ipod','ipad','iphone']
for line in sys.stdin:
    n+=1
    d_add = {}
    line = line.decode('utf8').split('\t')
    # print line[1].replace('\n','')
    cur_word = line[0]
    cur_count = line[1].replace('\n','')
    if cur_word in version or download or function or device:
        # print cur_word,cur_count
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
    # print k,v
    print ("{} {} {}".format(k, '\t',v).encode('utf8'))
# print n