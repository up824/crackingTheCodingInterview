# determin if a string has all unique char
def isUnique(s):
    charSet = set()
    for c in s:
        if c in charSet:
            return False
        charSet.add(c)

    return True

# follow up - no additional data structure - sorted s
def isUnique2(s):
    s = sorted(s)
    for i in xrange(len(s)):
        if i > 0 and s[i] == s[i - 1]:
            return False
    return True

# test
import unittest
class TestUnique(unittest.TestCase):
    trueCases = ['1', '', ' ', 'abcdefg']
    falseCases = ['  ', 'aa', 'abcdefga', 'dddddd']
    def test_unique(self):
        for case in self.trueCases:
            self.assertTrue(isUnique(case))
        for case in self.falseCases:
            self.assertFalse(isUnique(case))
    def test_unique2(self):
        for case in self.trueCases:
            self.assertTrue(isUnique2(case))
        for case in self.falseCases:
            self.assertFalse(isUnique2(case))


if __name__ == '__main__':
    print 'isUnique - T: O(n) / S: O(n)'
    print 'isUnique2 - T: O(nlogn) / S: O(1)'
    unittest.main()
