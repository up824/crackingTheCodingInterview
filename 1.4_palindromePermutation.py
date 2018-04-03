# 1.4 Palindrome permutation: check if a given string is a permutation of a parlindrom
def isParlindromePermutation(s):
    from collections import Counter
    counter = Counter(s.lower())
    del counter[' ']
    odd = 0
    for cnt in counter.values():
        if cnt % 2 == 1:
            if odd == 1:
                return False
            odd += 1
    return True

# test
import unittest
class  Test(unittest.TestCase):
    cases = [('Tact coa', True), ('abcbb', False), ('', True), ('abcba', True)]
    def test_isPP(self):
        for s, res in self.cases:
            self.assertEqual(isParlindromePermutation(s), res)

if __name__ == '__main__':
    unittest.main()
