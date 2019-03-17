# -*- coding: utf-8 -*-

from random import choice
from sys import stdin

txt = ''.join(stdin)
words = [i.lower() for i in txt.split()]
following = {}
for i in range(len(words)-1):
    following[words[i]] = following.get(words[i], [])+[words[i+1]]
following[words[-1]] = following.get(words[-1], [])


word = choice(list(following))
output = word.title()
while following[word]:
    print(word, end=' ')
    word = choice(following[word])
    output += ' ' + word

print(output)
