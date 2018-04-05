# 3.1 use a single array to implement three stacks
class Stack3(object):
    def __init__(self):
        self.arr = []
        self.idx = [-3, -2, -1]
        self.start = [-3, -2, -1]
        self.length = 0

    def push(self, val, stackIdx):
        self.idx[stackIdx] += 3
        if self.idx[stackIdx] >= len(self.arr):
            self.arr.extend([0] * 3)
        self.arr[self.idx[stackIdx]] = val

    def pop(self, stackIdx):
        try:
            res = self.peak(stackIdx)
        except:
            raise IndexError("can't pop item, stack is empty")
        self.idx[stackIdx] -= 3
        return res

    def isEmpty(self, stackIdx):
        if self.idx[stackIdx] == self.start[stackIdx]:
            return True
        else:
            return False

    def peak(self, stackIdx):
        if self.isEmpty(stackIdx):
            raise IndexError("can't peak item, stack is empty")
        return self.arr[self.idx[stackIdx]]

# test
import unittest
class Test(unittest.TestCase):
    def test_stack3(self):
        stack3 = Stack3()
        for i in xrange(100):
            stack3.push(i, 0)
        for i in xrange(99, -1, -1):
            self.assertEqual(stack3.pop(0), i)
        for i in xrange(1000):
            stack3.push(i, i % 3)
        for i in xrange(1000 - 1, -1, -1):
            self.assertEqual(stack3.pop(i % 3), i)

if __name__ == "__main__":
    unittest.main()
