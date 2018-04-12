# 5.6 Conversion
def conversion(a, b):
    c = a ^ b
    cnt = 0
    while c:
        cnt += 1
        c = c & (c - 1)
    return cnt

import unittest
class Test(unittest.TestCase):
    def test_conversion(self):
        a, b, res = 29, 15, 2
        self.assertEqual()
