#10.8 Find Duplicate array with number from 1 to N. Use 4kbytes mem to find all duplicates
"""
4kbytes
32k bits
32k bits can represent 32k int which is 32 * 1024 > 32000 numbers
use 4kbytes as a table
"""
def findDuplicate(arr):
    mem = [False] * (32000 + 1)
    #from 1 to 32000
    res = []
    for num in arr:
        if mem[num]:
            res.append(num)
        else:
            mem[num] = True

    return res

"""
or two pass
first 1 - 16000
second 16001 -32000
since the function and result take space
"""

class BitSet(object):
