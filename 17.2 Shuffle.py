#17.2 Shuffle
from random import randint
def shuffle(nums):
    n = len(nums)
    for i in xrange(n):
        j = randint(i, n - 1)
        nums[i], nums[j] = nums[j], nums[i]
    return nums

import collections
table = collections.defaultdict(lambda : collections.defaultdict(int))
for _ in xrange(10000):
    arr = shuffle(list(range(6)))
    for i, v in enumerate(arr):
        table[i][v] += 1
print table
