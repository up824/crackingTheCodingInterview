# 1.6 string compression aabcccccaaa -> a2b1c5a3
# T: O(n)  S: O(1)
def stringCompression(s):
    n = len(s)
    if n < 3:
        return s
    cnt = 1
    res = ''

    for i in xrange(1, n + 1):
        if s[i - 1] < 'a' or s[i - 1] > 'z':
            raise ValueError('should in range a-z')
        if i < len(s) and s[i] == s[i - 1]:
            cnt += 1
        else:
            res += s[i - 1] + str(cnt)
            cnt = 1

    return res if len(res) < n else s


import unittest
class Test(unittest.TestCase):
    def test_stringCompression(self):
        cases = [('aabcccccaaa', 'a2b1c5a3'), ('abcdefg', 'abcdefg'), ('aaaaa', 'a5')]
        exceptionCases = [('11bs', ValueError)]
        for s, res in cases:
            self.assertEqual(stringCompression(s), res)
        for s, ex in exceptionCases:
            with self.assertRaises(ex) as context:
                stringCompression(s)
            self.assertTrue('in range' in context.exception.message)

if __name__ == '__main__':
    unittest.main()
