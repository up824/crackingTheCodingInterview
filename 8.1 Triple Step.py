# 8.1 Triple step
def tripleStep(n):
    if n == 0:
        return 0
    one, two, three = 1, 2, 1
    if n == 1:
        return one
    if n == 2:
        return two

    for i in xrange(3, n + 1):
        curr = one + two + three
        one, two, three = curr, one, two
    return curr


import unittest
class Test(unittest.TestCase):
    def test_tripleStep(self):
        cases = [(0, 0) , (1, 1), (2, 2), (3, 4), (4, 7)]
        for n, res in cases:
            self.assertEqual(tripleStep(n), res)

if __name__ == "__main__":
    unittest.main()
