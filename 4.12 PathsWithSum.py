#4.12 Paths with Sum
def pathsWithSum(root, target):
    if not root:
        return []

    res = []
    path = []
    curr = root

    dfs(curr, path, target, res)

    return res

def dfs(root, path, target, res):
    if target == 0:
        vals = [node.val for node in path]
        res.append(vals)
    if not root:
        return
