#16.2 Word Frequencies
def wordFrequencies1(book, word):
    cnt = 0
    for w in book:
        if w == word:
            cnt += 1
    return cnt

import collections
def wordFrequencies2(book, word):
    table = collections.Counter(book)
    return table[word]

book = ['a','b','a','good']
book += ['good'] * 10

print wordFrequencies1(book, 'good')
print wordFrequencies2(book, 'good')
