# 3.3 Set of Stack
class SetOfStack(object):
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("capacity can't be less than 1")
        self.arr = []
        self.capacity = capacity

    def push(self, val):
        if self.isEmpty() or self.arr[-1].getSize() == self.capacity:
            self.arr.append(Stack())
        self.arr[-1].push(val)

    def pop(self):
        if self.isEmpty():
            raise IndexError("setOfStack is empty, can't pop")
        res = self.arr[-1].pop()
        while not self.isEmpty() and self.arr[-1].getSize() == 0:
            self.arr.pop()
        return res

    def isEmpty(self):
        return len(self.arr) == 0

    def peak(self):
        if self.isEmpty():
            raise IndexError("SetOfStack is empty, can't peak")
        return self.arr[-1].peak()

    def popAt(self, index):
        if index >= len(arr):
            raise IndexError("incorrect Index, current size is " + str(len(arr)))
        if self.arr[index].getSize() == 0:
            raise IndexError("target stack is empty")
        return self.arr[index].pop()


class Stack(object):
    def __init__(self):
        self.arr = []

    def getSize(self):
        return len(self.arr)

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if self.isEmpty():
            raise IndexError("stack is empty, can't pop")
        return self.arr.pop()

    def peak(self):
        if self.isEmpty():
            raise IndexError("stack is empty, can't peak")
        return self.arr[-1]

    def isEmpty(self):
        return len(self.arr) == 0


import unittest
class Test(unittest.TestCase):
    def test_SetOfStack(self):
        SS = SetOfStack(1)
        for i in xrange(100):
            SS.push(i)
        for i in xrange(99, -1, -1):
            #print SS.peak()
            self.assertEqual(SS.pop(), i)

if __name__ == "__main__":
    unittest.main()
