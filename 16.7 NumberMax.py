#16.7 Number Max
def numberMax(a, b):
    nums = [a, b]
    sel = ((a - b) >> 31) & 1
    return nums[sel]

print numberMax(23, 21)
