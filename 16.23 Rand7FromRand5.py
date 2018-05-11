#16.23 Rand7 from Rand5
from random import randint
def rand7FromRand5():
    res = rand2() * 4 + rand2() * 2 + rand2()
    if res == 7:
        rand7FromRand5()
    return res

def rand2():
    res = rand5()
    while res > 1:
        res = rand5()
    return res

def rand5():
    return randint(0, 4)

import collections
counter = collections.Counter()
for _ in xrange(10000):

    num = rand7FromRand5()
    counter[num] += 1
print counter
