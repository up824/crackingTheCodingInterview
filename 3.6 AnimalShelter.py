# 3.6 Animal Shelter, implement enqueue, dequeueAny, dequeueDog, dequeueCat
class AnimalShelter(object):
    def __init__(self):
        self.queue = Queue()
        self.catQueue = Queue()
        self.dogQueue = Queue()
        self.catCnt = 0
        self.dotCnt = 0

    def enqueue(self, val):
        self.queue.psuh(val)

    def dequeueAnry(self):
        try:
            res = self.queue.pop()
        except IndexError:
            raise IndexError("No aminal for adopt, please check again later")

        if not self.catQueue.isEmpty() and  res == self.catQueue.peak():
            self.catQueue.pop()

        if not self.dogQueue.isEmpty() and  res == self.dogQueue.peak():
            self.dogQueue.pop()

    def dequeueCat(self):


    def dequeueDog(self):

    # def _x(x):

class Queue(object):
    def __init__(self, val):
        self.arr = []
        self.start = self.end = 0

    def push(self, val):
        self.arr.append(val)
        self.end += 1

    def pop(self):
        try:
            res = self.peak()
        except IndexError:
            raise IndexError("Queue is empty, can't pop")
        self.start += 1
        return res

    def peak(self):
        if self.isEmpty():
            raise IndexError("Queue is empty, can't peak")
        return self.arr[self.start]

    def isEmpty(self):
        return self.start == self.end
