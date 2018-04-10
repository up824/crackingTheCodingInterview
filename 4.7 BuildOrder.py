# 4.7 Build order
def buildOrder(dependencies):
    if not dependencies:
        return []

    res = []
    prevTable = collections.defaultdict(int)
    nextTable = collections.defaultdict(set)
    courses = set()
    for prev, curr in dependencies:
        prevTable[curr] += 1
        nextTable[prev].add(curr)
        courses.update(set([prev, curr]))

    queue = collections.deque()
    for course in courses:
        if course not in prevTable.keys():
            queue.append(course)


    while queue:
        curr = queue.popleft()
        res.append(curr)
        for next in nextTable[curr]:
            prevTable[next] -= 1
            if prevTable[next] == 0:
                queue.append(next)

    if len(res) == len(courses):
        return res

    raise ValueError("no valid order found")
