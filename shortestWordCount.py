#!/usr/bin/env python

import re,sys

n = 100
text = open('test.txt','r').read().lower()
words={}
parsed_text = re.findall("\w+-\w+-\w+|\w+-\w+|[\w']+",text)

for word in parsed_text:
    if word[0].isalpha(): 
    	words[word]=words.setdefault(word,0)+1

"Total Words: %i" %len(text.split())
"Total UNIQUE Words: %i\n" %len(words)
counter = 1
for key in sorted(words.keys(), key= lambda k: words[k],reverse=True):
    if counter <= n:
        print str(counter)+') ', key, '-', words[key], 'times'
        counter += 1
