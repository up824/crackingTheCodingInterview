# 8.4
def powerSet(arr):
    arr.sort()
    path = []
    res = []
    start = 0
    dfs(start, arr, path, res)
    return res

def dfs(start, arr, path, res):

    if start > len(arr):
        return

    res.append(path[:])

    for i in xrange(start, len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        dfs(i + 1, arr, path + [arr[i]], res)

if __name__ == "__main__":
    print powerSet([1, 2, 3, 4])
