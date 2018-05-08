#16.19 Pond Size
def pondSize(matrix):
    def paint(i, j):
        import collections
        queue = collections.deque()
        queue.append((i, j))
        cnt = 1
        matrix[i][j] = 1
        while queue:
            ii, jj = queue.popleft()
            for di, dj in directions:
                ni, nj = ii + di, jj + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == 0:
                    matrix[ni][nj] = 1
                    cnt += 1
                    queue.append((ni, nj))
        return cnt


    res = []
    if not matrix or not matrix[0]:
        return res
    m, n  = len(matrix), len(matrix[0])

    directions = [(i, j) for i in (0, -1, 1) for j in (0, -1, 1) if not (i == 0 and j == 0)]
    for i in xrange(m):
        for j in xrange(n):
            if matrix[i][j] == 0:
                res.append(paint(i, j))

    return res

matrix = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
print pondSize(matrix)
