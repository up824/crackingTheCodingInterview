# 2.8 detect circle
def loopDections(head):
    if not head:
        return None

    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    if not fast or not fast.next:
        return None

    curr = head
    while curr != slow:
        curr, slow = curr.next, slow.next
    return curr
