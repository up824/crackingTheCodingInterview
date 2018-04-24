from collections import defaultdict, deque
def answer(dimensions, your_position, guard_position, distance):

    myPos, guardPos = tuple(your_position), tuple(guard_position)
    selfDirectTable, guardDirectTable = defaultdict(lambda:float("inf")), defaultdict(lambda:float("inf"))
    direct, dis = getDisInfo(myPos, guardPos)
    guardDirectTable[direct] = dis
    bfs(myPos, [guardPos], guardDirectTable, distance, dimensions)
    x, y = dimensions
    avoidPos = [myPos] + [(0, 0), (0, y), (x, 0), (x, y)]
    bfs(myPos, avoidPos, selfDirectTable, distance, dimensions)

    directions = 0
    for key, val in guardDirectTable.items():
        if key not in selfDirectTable:
            directions += 1
        else:
            if val < selfDirectTable[key]:
                directions += 1

    return directions


def bfs(start, dests, table, distance, dimensions):
    queue = deque()
    queue.extend(dests)
    visited = set()
    for dest in dests:
        visited.add(dest)

    while queue:
        curr = queue.popleft()
        nexts = getNexts(curr, dimensions)
        for nxt in nexts:
            if nxt in visited:
                continue
            direct, dis = getDisInfo(start, nxt)
            if 0 < dis <= distance ** 2:
                table[direct] = min(table[direct], dis)
                queue.append(nxt)
                visited.add(nxt)

def getNexts(curr, dimensions):
    x, y = dimensions
    i, j = curr

    bottom = (j // y) * y
    up = ceil(j, y) * y
    left = (i // x) * x
    right = ceil(i, x) * x

    deltaBottom = j - bottom
    deltaUp = up - j
    deltaLeft = i - left
    deltaRight = right - i

    nexts = [
             (ii, jj) for ii in (i, left - deltaLeft, right + deltaRight)
             for jj in (j, up + deltaUp, bottom - deltaBottom)
             if not (ii == i and jj == j)
            ]
    return nexts

def ceil(a, b):
    return -(-a // b)

def getDisInfo(start, end):

    x1, y1 = start
    x2, y2 = end

    deltaY = y2 - y1
    deltaX = x2 - x1

    if deltaY == 0 and deltaX == 0:
        direction = (0, 0)
        dis = 0
        return direction, dis

    mGCD = abs(gcd(deltaX, deltaY))

    direction = (deltaX / mGCD, deltaY / mGCD)
    dis = deltaY ** 2 + deltaX ** 2

    return direction, dis

def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)



#d, m, g, ddd = [3,2], [1,1], [2, 1], 4
d, m, g, ddd = [300, 275], [150, 150], [185, 100], 500
print answer(d, m, g, ddd)
