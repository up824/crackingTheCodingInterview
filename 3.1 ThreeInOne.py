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
            res = self.peak(stackIdx):
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
