# 3.2 Stack Min: min func which returns the minimum element in O(1)

class MinStack(object):
    def __init__(self):
        self.arr = []

    def push(self, val):
        try:
            prevMin = self.minElem()
        except:
            prevMin = float("inf")

        currMin = min(prevMin, val)
        self.arr.append((val, currMin))

    def pop(self):
        try:
            res = self.peak()
        except IndexError:
            raise IndexError("stack is empty, can't pop")
        self.arr.pop()
        return res

    def isEmpty(self):
        return len(self.arr) == 0

    def minElem(self):
        if self.isEmpty():
            raise IndexError("can't get min element, stack is empty")
        return self.arr[-1][1]

    def peak(self):
        if self.isEmpty():
            raise IndexError("stack is empty, can't peak")
        return self.arr[-1][0]
