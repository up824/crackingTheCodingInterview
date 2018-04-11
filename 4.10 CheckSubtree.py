#4.10 Check subtree
def checkSubtree(t1, t2):
    def preorder(root):
        if not root:
            return "#"
        res = str(root.val)

        left = preorder(root.left)
        right = preorder(root.right)
        res += "," + left + "," + right

        return res

    s1, s2 = "," + preorder(t1), "," + preorder(t2)
    return s2 in s1
