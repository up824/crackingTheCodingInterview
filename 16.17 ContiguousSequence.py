#16.17 Contiguous Sequence
def contiguousSeq(nums):
    res = curr = nums[0]
    for num in nums[1:]:
        curr = max(curr + num, num)
        res = max(res, curr)
    return res

import unittest
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(contiguousSeq([2, -8, 3, -2, 4, -10]), 5)

if __name__ == "__main__":
    unittest.main()
