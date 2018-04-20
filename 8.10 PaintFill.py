# 8.10 Paint Fill
from collections import deque
def paintFill(screen, color, point):
    if not screen or not screen[0]:
        raise IndexError("screen is empty")
    m, n = len(screen), len(screen[0])
    if not point or not(0 <= point[0] < m and 0 <= point[1] < n):
        raise IndexError("point is invalid")

    queue = deque()
    queue.append(point)
    origColor = screen[point[0]][point[1]]
    screen[point[0]][point[1]] = color

    while queue:
        i, j = queue.popleft()
        for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ii < m and 0 <= jj < n and screen[ii][jj] == origColor:
                screen[ii][jj] = color
                queue.append([ii, jj])

screen = [[1, 0, 2], [0, 0, 0]]
color = 3
point = [0, 1]
paintFill(screen, color, point)
print screen
