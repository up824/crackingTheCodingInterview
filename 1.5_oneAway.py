# 1.5 check if two str are 1 edit distance
def oneAway(a, b):
    # insert, del, replace
    lenA, lenB = len(a), len(b)
    if abs(lenA - lenB) > 1:
        return False

    for i in xrange(min(lenA, lenB)):
        if a[i] != b[i]:
            # del a
            if a[i + 1:] == b[i:]:
                return True
            # insert a
            if a[i:] == b[i + 1:]:
                return True
            # replace a
            if a[i + 1:] == b[i + 1:]:
                return True
            return False

    return True

import unittest
class Test(unittest.TestCase):
    def test_oneAwasy(self):
        cases = [('a', '', True), ('a', 'b', True), ('a', 'ab', True),
        ('abcdef', 'bcdef', True), ('','', True), ('abc', 'df', False),
        ('abab', 'ba', False), ('', 'cc', False), ('absdgdssdf', 'absdgdsssdff', False)]

        for a, b, res in cases:
            self.assertEqual(oneAway(a, b), res)

if __name__ == '__main__':
    unittest.main()
