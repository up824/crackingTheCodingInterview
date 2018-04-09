# 4.5 Validate BST
def isBST(root):

    def validateRoot(curr, minVal, maxVal):
        if not curr:
            return True
        if curr.val > maxVal or curr.val <= minVal: # depends on how you define BST
            return False
        left = validateRoot(curr.left, minVal, min(maxVal, root.val))
        right = validateRoot(curr.right, max(minVal, root.val), maxVal)
        return left and right

    return validateRoot(root, float("-inf"), float("inf"))
