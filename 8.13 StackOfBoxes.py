# 8.13 Stack of Boxes
import collections
def stackOfBoxes(boxes):
    # suppose box is a tuple with (w, d, h)
    boxes.sort(reverse = True)

    mem = collections.defaultdict(int)
    last = (float("inf"), float("inf"), float("inf"))
    h =  dfs(boxes, mem, 0, last)

    return h

def dfs(boxes, mem, curr, last):
    # return max height
    if not boxes:
        return curr
    if (last, curr) in mem:
        return mem[(last, curr)]

    maxHeight = curr
    # valid boxes and not visited
    for i, box in enumerate(boxes):
        if validSize(box, last):
             newHeight = dfs(boxes[i + 1:], mem, curr + box[2], box)
             maxHeight = max(maxHeight, newHeight)

    mem[(last, curr)] = maxHeight
    return maxHeight



def validSize(up, down):
    if up[0] <= down[0] and up[1] <= down[1]:
        return True
    return False


print stackOfBoxes([(1,1,1), (2,2,2), (3,3,3), (4, 2, 1), (1,2,1)])
