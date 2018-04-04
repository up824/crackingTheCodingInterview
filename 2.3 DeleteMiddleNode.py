# 2.3 delete a given middle node(not first or last)
class ListNode(object):
    def __init__(val):
        self.val = val
        self.next = None

def deleteMiddleNode(mid, head):
    # return void
    if not head or not head.next:
        return

    prev, curr = head, head.next

    while curr != mid:
        if not curr:
            return
        prev, curr = curr, curr.next

    prev.next = prev.next.next
