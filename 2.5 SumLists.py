# 2.5 Sum from LSB to MSB and from MSB to LSB
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.node = None

def sumList(a, b):
    dummy = ListNode(-1)
    head = dummy
    carry = 0
    while a or b or carry:
        valA = valB = 0
        if a:
            valA = a.val
            a = a.next
        if b:
            valB = b.val
            b = b.next

        sumVal = valA + valB + carry
        carry, val = sumVal / 10, sumVal % 10
        head.next = ListNode(val)

        head = head.next

    return dummy.next

def sumList2(a, b):
    a = reverse(a)
    b = reverse(b)
    res = sumList(a, b)
    res = reverse(res)
    return res

def reverse(head):
    if not head:
        return head

    prev = None
    while head:
        head.next, head, prev = prev, head.next, head
    return prev
