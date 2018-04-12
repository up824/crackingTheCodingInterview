# 5.2 binary to string
def binaryToString(n):
    if n < 0 or n >= 1:
        return "ERROR"
    res = "0b0."
    cnt = 0
    while n and cnt < 32:
        if 2 * n >= 1:
            res += "1"
            n = n * 2 - 1
        else:
            res += "0"
            n = n * 2
        cnt += 1
    if n == 32 and n != 0:
        return "ERROR"
    return res

import unittest
class TEST(unittest.TestCase):
    def test_binaryToString(self):
        n = 0.125
        res = "0b0.001"
        self.assertEqual(binaryToString(n), res)

if __name__ == "__main__":
    unittest.main()
