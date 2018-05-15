#17.12 BiNode
class BiNode(object):
    def __init__(self, data):
        self.data = x
        self.prev = None
        self.next = None

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def convert(root):

    def helper(root):
        # return head and tail
        head, tail = None, None
        if not root:
            return head, tail

        leftHead, leftTail = convert(root.left)
        rightHead, rightTail = convert(root.right)

        curr = BiNode(root.data)
        if leftHead:
            leftTail.next = curr
            head = leftHead
        else:
            head = curr

        if rightHead:
            curr.next = rightHead
            tail = rightTail
        else:
            tail = curr

        return head, tail

    h, t = helper(root)
    return h
