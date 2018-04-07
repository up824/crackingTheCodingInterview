# 4.2 Minimal Tree
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def minimalTree(arr):
    if not arr:
        return None

    m = len(arr) / 2
    root = TreeNode(arr[m])
    root.left = self.minimalTree(arr[:m])
    root.right = self.minimalTree(arr[m + 1:])
    return root
