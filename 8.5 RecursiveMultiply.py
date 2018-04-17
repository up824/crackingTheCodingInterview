# 8.5 RecursiveMultiply
def recursiveMutliply(a, b):
    # make sure a is not smaller than b
    if a < b:
        a, b = b, a
    if b == 0:
        return 0
    if b == 1:
        return a
    if b == 2:
        return a + a

    half = recursiveMutliply(a, b/2)
    remainder = recursiveMutliply(a, b % 2)

    return half + half + remainder

import unittest
import random
class Test(unittest.TestCase):
    def test_recursiveMult(self):
        for _ in xrange(100):
            a, b = random.randint(0, 100), random.randint(0, 100)
            res = a * b
            self.assertEqual(recursiveMutliply(a, b), res)

if __name__ == "__main__":
    unittest.main()
