# 4.8 First Common Ancestor
def firstCommonAncestor(root, a, b):
    if not root:
        return root

    if root == a or root == b:
        return root

    left = firstCommonAncestor(root.left, a, b)
    right = firstCommonAncestor(root.right, a, b)

    if left and right:
        return root

    return left or right
