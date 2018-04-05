#2.2 return kth to last from LL
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def returnKthToLast(head, k):
    if not head or k < 1:
        return head
    node = head
    while k:
        if not node:
            return None
        k -= 1
        node = node.next
    res = head
    while node:
        node, res = node.next, res.next
    return res
