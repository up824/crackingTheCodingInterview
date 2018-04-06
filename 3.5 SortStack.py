# 3.5 SortStack
class Stack(object):
    def __init__(self):
        self.arr = []

    def push(self, val):
        self.arr.append(val)

    def peak(self):
        if self.isEmpty():
            raise IndexError("Stack is empty, can't peak")
        return self.arr[-1]

    def isEmpty(self):
        return len(self.arr) == 0

    def pop(self):
        try:
            res = self.peak()
        except IndexError:
            raise IndexError("Stack is empty, can't pop")

        self.arr.pop()
        return res

class SortStack(object):
    def __init__(self):
        self.stack = Stack()

    def push(self, val):
        if self.isEmpty() or self.stack.peak() >= val:
            self.stack.push(val)
            return

        tmpStack = Stack()
        while not self.stack.isEmpty() and self.stack.peak() < val:
            tmpStack.push(self.stack.pop())

        self.stack.push(val)
        while not tmpStack.isEmpty():
            self.stack.push(tmpStack.pop())

    def pop(self):
        try:
            res = self.stack.pop()
        except IndexError:
            raise IndexError("SortStack is empty, can't pop")
        return res

    def peak(self):
        try:
            res = self.stack.peak()
        except IndexError:
            raise IndexError("SortStack is empty, can't peak")
        return res

    def isEmpty(self):
        return self.stack.isEmpty()

#test
import unittest
class Test(unittest.TestCase):
    def test_SortStack(self):
        sortStack = SortStack()
        for i in xrange(100):
            sortStack.push(i)
            self.assertEqual(sortStack.peak(), 0)
        for i in xrange(100):
            self.assertEqual(sortStack.pop(), i)


if __name__ == "__main__":
    unittest.main()
