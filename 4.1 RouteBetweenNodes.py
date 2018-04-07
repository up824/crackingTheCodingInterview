# 4.1 Route Between Nodes
class GraphNode(object):
    def __init__(val):
        self.val = val
        self.neighbors = []

def routeBetweenNodes(nodeA, nodeB):
    if not nodeA or not nodeB:
        return False

    queue = collections.deque()
    queue.append(nodeA)
    visited = set(nodeA)
    while queue:
        curr = nodeA
        for neighbor in curr.neighbors:
            if neighbor in visited:
                continue
            if neighbor == nodeB:
                return True
            queue.append(neighbor)
            visited.add(neighbor)
    return False
