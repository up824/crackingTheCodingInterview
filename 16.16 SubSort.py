#16.16 Sub Sort
def subSort(nums):
    n = len(nums)
    if n == 1:
        return []
    start, end = 0, n - 1
    while start + 1 <= end and nums[start + 1] >= nums[start]:
        start += 1
    if start == end:
        return []
    while end - 1 >= start and nums[end - 1] <= nums[end]:
        end -= 1
    nn, m = start, end

    for i in xrange(nn + 1, n):
        while start >= 0 and nums[i] < nums[start]:
            start -= 1

    for i in xrange(m, -1, -1):
        while end < n and nums[i] > nums[end]:
            end += 1

    return [start + 1, end - 1]


import unittest
class Test(unittest.TestCase):
    def test_subSort(self):
        input = [1, 2, 4, 7, 10, 11, 7 , 12, 6, 7, 16, 18, 19]
        output = [3, 9]
        self.assertEqual(subSort(input), output)

if __name__ == "__main__":
    unittest.main()
