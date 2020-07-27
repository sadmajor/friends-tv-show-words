import glob, os, re

from collections import Counter

words = []
for filename in glob.glob('**/*.DVDRip.S*'):
    with open(filename, 'r') as sub:
        for line in sub.readlines():
            words += re.sub("[^A-Za-z]", " ",  line).split()


a =[x.lower() for x in words]

final = []
for elem, count in Counter(a).iteritems():
    if count <= 10 and count >= 2:
        final.append(elem)
print(len(final))
print(final[:100])