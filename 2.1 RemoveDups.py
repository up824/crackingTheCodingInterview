#2.1 Remove Duplicates in a linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDup(head):
    if not head:
        return

    node = head
    hashSet = set() 

    while node.next:
        nxt = node.next
        if nxt.val in hashSet():
            # remove
            node.next = nxt.next
        else:
            hashSet.add(nxt.val)
            node = nxt

def removeDup2(head):
    if not head:
        return

    node = head

    while node:
        curr = node
        while curr.next:
            nxt = curr.next
            if nxt.val == node.val:
                curr.next = nxt.next
            else:
                curr = nxt
        node = node.next
