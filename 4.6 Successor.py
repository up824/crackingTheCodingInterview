# 4.6 Successor in-order successor in BST, each node has a link to its parent
class TreeNode(object):
    def __init__(val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

def successor(root):
    if not root:
        return root

    succ = None
    if root.right:
        curr = root.right
        while curr:
            if root.val < curr.val:
                succ = curr
                curr = curr.left
            else:
                curr = curr.right
        return succ

    curr = root.parent
    while curr:
        if curr.val > root.val:
            return curr
        curr = curr.parent

    return succ
