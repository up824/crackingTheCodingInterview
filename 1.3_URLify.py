# 1.3 URLify replace all spaces in a string wth '%20'
# assumption: 1. sufficient space at the end
# example- in: "Mr John Smith   ", 13 -> "Mr%20John%20Smith"
def URLify(s, length):
    # return a string
    s = s[:length]
    return '%20'.join(s.split())

# not pythonic
def URLify2(s, length):
    res = ''
    for i in xrange(length):
        if s[i] == ' ':
            if i > 0 and s[i - 1] == ' ':
                continue
            res += '%20'
        else:
            res += s[i]
    return res

import unittest
class Test(unittest.TestCase):
    cases = [('Mr John Smith    ', 13, 'Mr%20John%20Smith')]
    def test_URLify(self):
        for s, l, res in self.cases:
            self.assertEqual(URLify(s, l), res)
    def test_URLify2(self):
        for s, l, res in self.cases:
            self.assertEqual(URLify2(s, l), res)

if __name__ == '__main__':
    unittest.main()
