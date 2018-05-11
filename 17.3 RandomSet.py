#17.3 Random Set
from random import randint
def randomSet(nums, m):
    n = len(nums)
    m = min(m, n)
    for i in xrange(m):
        j = randint(i, n - 1)
        nums[i], nums[j] = nums[j], nums[i]
    return set(nums[:m])

print randomSet(list(range(6)),4)
