# 1.2 check permutation. given two strings, detect if one is a permutation of the other
# 1. O(1) Space, O(max(a,b)log(max(a,b))) Time
def checkPermutation(a, b):
	sortedA, sortedB = sorted(a), sorted(b)
	return sortedA == sortedB

# O(max(a, b)) Space, O(max(a, b)) Time
from collections import Counter
def checkPermutation2(a, b):
	counter = Counter(a)
	for c in b:
		counter[b] -= 1
	return sum(counter.values()) == 0

# test
import unittest
class Test_checkPermutation(unittest.TestCase):
	cases = [(' ', ' ', True), ('a', 'a', True), ('a','ab', False),
	('abc', 'cba', True), ('', '', True), ('aaa', 'aa', False), ('efdsf','ffdse', True)]

	def test_checkPermutation(self):
		for a, b, result in self.cases:
			self.assertEqual(checkPermutation(a, b), result)
	def test_checkPermutation2(self):
		for a, b, result in self.cases:
			self.assertEqual(checkPermutation2(a, b), result)

if __name__ == '__main__':
	unittest.main()
