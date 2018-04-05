# 2.7 Intersection
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def intersection(a, b):
    if not a or not b:
        return None

    headA, headB = a, b
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA

    return a

def intersection2(a, b):
    if not a or not b:
        return None

    headA, headB = a, b
    nA = nB = 0
    while a:
        a, nA = a.next, nA + 1
    while b:
        b, nB = b.next, nB + 1
    diff = abs(nA - nB)
    a, b = headA, headB
    if nA > nB:
        for _ in xrange(diff):
            a = a.next
    else:
        for _ in xrange(diff):
            b = b.next
    while a != b:
        a = a.next
        b = b.next
    return a
