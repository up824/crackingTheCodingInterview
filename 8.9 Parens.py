# 8.9 Parens
def parens(n):
    res = []
    curr = ""
    dfs(n, n, curr, res)
    return res

def dfs(l, r, curr, res):
    if l == 0 and r == 0:
        res.append(curr)
        return

    if l > 0:
        dfs(l - 1, r, curr + "(", res)
    if r > 0 and l < r:
        dfs(l, r - 1, curr + ")", res)

print parens(3)
