# 1.9 String Rotation you have a method isSubstring. Use this method only once to figure out if s2 is a rotation of s1

def isSubstring(a, b):
    # if a is a substring of b
    return a in b

def stringRotation(a, b):
    # return bool
    # tip : use isSubString means you need to build a new string larger than original one, in this case, double it
    # check if b is a rotation of a
    if not a and not b:
        return True
    if not a or not b:
        return False
    lenA, lenB = len(a), len(b)
    if lenA != lenB:
        return False
    return isSubstring(b, a * 2)


# test
import unittest
class Test(unittest.TestCase):
    def test_stringRotation(self):
        cases = [('waterbottle', 'erbottlewat', True), ('a', 'a', True), ('', 'b', False),
        ('', '', True), (' ', '', False), ('aaab', 'baaa', True), ('abc', 'def', False)]
        for a, b, res in cases:
            #print a, b ,res
            self.assertEqual(stringRotation(a, b), res)

if __name__ == '__main__':
    unittest.main()
