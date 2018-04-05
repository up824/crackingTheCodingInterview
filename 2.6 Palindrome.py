# 2.6 Palindrome
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

def isPalindrome(head):
    if not head or not head.next:
        return True

    # 1. split & reverse first half
    fast = slow = head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        slow.next, slow, prev = prev, slow.next, slow

    # keep prev and curr
    left, right = prev, slow

    prev = slow
    if fast:
        # odd case
        right = right.next


    res = True
    while left and right:
        if left.val != right.val and res:
            res = False
        right = right.next
        left.next, left, prev = prev, left.next, left

    return res
