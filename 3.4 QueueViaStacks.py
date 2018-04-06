# 3.4 build a queue with 2 stacks
class Queue(object):
    def __init__(self):
        self.stacks = [Stack(), Stack()]

    def push(self, val):
        self.stacks[0].push(val)

    def pop(self):
        if self.isEmpty():
            raise IndexError("Queue is empty, can't pop")
        res = self.peak()
        self.stacks[-1].pop()
        return res

    def peak(self):
        if self.isEmpty():
            raise IndexError("Queue is empty, can't peak")
        if self.stacks[-1].isEmpty():
            while not self.stacks[0].isEmpty():
                self.stacks[-1].push(self.stacks[0].pop())
        return self.stacks[-1].peak()

    def isEmpty(self):
        return self.stacks[0].isEmpty() and self.stacks[-1].isEmpty()

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

import unittest
class Test(unittest.TestCase):
    def test_Queue(self):
        queue = Queue()
        for i in xrange(100):
            queue.push(i)
        for i in xrange(100):
            self.assertEqual(queue.pop(), i)

if __name__ == "__main__":
    unittest.main()
