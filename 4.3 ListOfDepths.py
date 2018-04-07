# 4.3 List of Depths

class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def listOfDepths(root):
    res = []
    if not root:
        return res

    queue = collections.deque()
    queue.append(root)

    while queue:
        dummy = ListNode(-1)
        head = dummy
        size = len(queue)
        for _ in xrange(size):
            curr = queue.popleft()
            head.next = ListNode(curr.val)
            head = head.next
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        res.append(dummy.next)
    return res
