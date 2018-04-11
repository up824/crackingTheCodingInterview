#4.9 BST sequence
def bstSequence(root):
    def dfs(nexts):
        if not nexts:
            vals = [node.val for node in path]
            res.append(vals)
            return

        for i, nxt in enumerate(nexts):
            path.append(nxt)
            newNexts = []
            if nxt.left:
                newNexts.append(nxt.left)
            if nxt.right:
                newNexts.append(nxt.right)
            dfs(nexts[:i] + newNexts + nexts[i + 1:])
            path.pop()

    res = []
    path = []

    dfs([root])

    return res
