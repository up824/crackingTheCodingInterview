# 4.4 Check Balanced
def isBalanced(root):
    def dfs(curr):
        if not curr:
            return 0
        left = dfs(curr.left)
        right = dfs(curr.right)
        if abs(left - right) > 1:
            res[0] = False
        return max(left, right) + 1

    res = [True]

    dfs(root)

    return res[0]
