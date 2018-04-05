# 2.4 partition a ll, val < x in first part  val >= x in the other part
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def partition(x, head):
    if not head:
        return
    dummy, xhead = ListNode(-1), ListNode(-1)
    dummy.next = head
    currX = xhead
    curr = dummy

    while curr.next:
        nxt = curr.next
        if nxt.val >= x:
            # assign
            currX.next = nxt
            # remove
            curr.next = nxt.next
            # clean tail
            nxt.next = None
            # next
            currX = currX.next
        else:
            curr = curr.next

    curr.next = xhead.next
