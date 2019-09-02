import re
import sys

inputFname = sys.argv[1]
outputFname = sys.argv[2]

word_count = dict()
tempWord = ''

with open(inputFname) as f:

    text = f.read()

    for chr in ' -:.\',;':
        text = text.replace(chr, ' ')

    text = text.lower()

    for word in text.split():
        if len(word) <= 0:
            continue
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

with open(outputFname, 'w') as f:
    for key in sorted(word_count):
        f.write(key + ' ' + str(word_count[key]) + '\n')
