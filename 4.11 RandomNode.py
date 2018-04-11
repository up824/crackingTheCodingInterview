# 4.11 random node
def randomNode(root):
    if not root:
        return None
    queue = collections.deque()
    queue.append(root)
    n = 0
    res = None
    while queue:
        curr = queue.popleft()
        n += 1
        if random.randint(1, n) == 1:
            res = curr
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return res
