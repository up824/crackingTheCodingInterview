# 8.2 robot in a grid
def robot(r, c, barriers):
    res = []
    dfs((0, 0), r, c, barriers, [(0, 0)], res)
    return res

def dfs(curr, r, c, barriers, path, res):
    if res:
        return
    if r == 0 and c == 0:
        res.append(path)
        return
    x, y = curr
    if r > 0:
        if (x + 1, y) not in barriers:
            dfs((x + 1, y), r - 1, c, barriers, path + [(x + 1, y)], res)

    if not res and c > 0:
        if (x, y + 1) not in barriers:
            dfs((x, y + 1), r, c - 1, barriers, path + [(x, y + 1)], res)

if __name__ == "__main__":
    print robot(5, 4, ((2,0), (1,2), (3, 3)))
