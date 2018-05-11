#16.24 Pairs with Sum
from collections import defaultdict
def pairsWithSum(nums, target):
    table = defaultdict(list)
    res = []
    for i,num in enumerate(nums):
        if target - num in table:
            prevIndexes = table[target - num]
            for idx in prevIndexes:
                res.append((idx, i))
        table[num].append(i)
    return res

print pairsWithSum([1,1,2,3,4,5,6,0,5,4], 5)
