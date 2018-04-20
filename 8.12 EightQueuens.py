#8.12 Eight Queuens
def eightQueuens():
    path = []
    res = []
    start = 0
    dfs(path, res)
    return res

def dfs (path, res):
    if len(path) == 8:
        res.append(path)
        return

    curr = len(path)
    for i in xrange(8):
        if i in path:
            continue
        skip = False
        for j in xrange(len(path)):
            if curr - j == abs(i - path[j]):
                skip = True
                break
        if not skip:
            dfs(path + [i], res)

print len(eightQueuens())
print eightQueuens()
