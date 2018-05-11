#16.21 Sum Swap
def sumSwap(a, b):
    if not a or not b:
        return []
    if len(a) < len(b):
        return sumSwap(b, a)

    sumA, sumB = sum(a), sum(b)
    diff = sumA - sumB
    if diff % 2 == 1:
        return []
    hashSet = set(b)
    #print diff, hashSet
    for aa in set(a):
        if aa - diff / 2 in hashSet:
            return [aa, -(aa + diff)]
    return []

import unittest
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sumSwap([4,1,2,1,1,2], [3,6,3,3]), [1,3])

if __name__ == "__main__":
    unittest.main()
