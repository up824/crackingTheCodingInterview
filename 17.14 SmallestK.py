#17.14 Smallest K
from heapq import *
def smallestK(nums, k):
    n = len(nums)
    if n == 0 or k == 0:
        return []
    if n <= k:
        return nums[:]

    h = [-num for num in nums[:k]]
    heapify(h)

    for i in xrange(k, n):
        num = -nums[i]
        if num > h[0]:
            heapreplace(h, num)

    for i in xrange(k):
        h[i] = -h[i]

    return h

print smallestK([1,2,6,8,4,0,-2,-3], 4)
