#5.1 Insertion
def insert(N, M, i, j):
    # insert M into N
    # assum j is larger than i
    if i > j:
        i, j = j, i

    allOne = 2 ** 32 - 1
    left = (allOne << (j + 1)) & allOne
    right = allOne >> (32 - i)
    mask = left | right
    N = N & mask
    return N | (M << i)

import unittest
class Test(unittest.TestCase):
    def test_insert(self):
        cases = [(0b10000000000, 0b10011, 2, 6, 0b10001001100)]
        for N, M, i, j, res in cases:
            self.assertEqual(insert(N, M, i, j), res)

if __name__ == "__main__":
    unittest.main()
