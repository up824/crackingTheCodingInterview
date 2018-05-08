#16.18  patternMatching
import collections
def patternMatching(s, pattern):



import unittest
class Test(unittest.TestCase):
    def test(self):
        cases = [("catcatgocatgo", "aabab", True),
        ("catcatgocatgo", "ab", True),
        ("catcatgocatgo", "a", True),
        ("catcatgocatgo", "aababb", False)]
        for s, pattern, res in cases:
            print s, pattern, res
            self.assertEqual(patternMatching(s, pattern), res)

if __name__ == "__main__":
    unittest.main()
