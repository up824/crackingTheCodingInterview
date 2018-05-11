#17.1 Add without Plus
def addWithoutPlus(a, b):
    while a != 0:
        b, a = a ^ b, (a & b) << 1
    return b


import unittest, random
class Test(unittest.TestCase):
    def test(self):
        for _ in xrange(100):
            a, b = random.randint(0, 100), random.randint(0, 100)
            self.assertEqual(addWithoutPlus(a, b), a + b)

if __name__ == "__main__":
    unittest.main()
