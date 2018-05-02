#16.6 Smallest Difference
def findSmallestDiff(a, b):
    na, nb = len(a), len(b)
    if na == 0 or nb == 0:
        return -1, -1
    if na > nb:
        a, b = b, a
        na, nb = nb, na

    a.sort()
    b.sort()
    minDiff = float("inf")
    l, r = -1, -1
    for i in a:
        if i > b[-1] and i - b[-1] > minDiff:
            break
        diff, ib = _find(i, b)
        if diff == 0:
            return i, ib
        if diff < minDiff:
            l, r = i, ib
            minDiff = diff

    return l, r

def _find(i, b):
    start, end = 0, len(b) - 1
    diff = float("inf")
    ib = -1
    while start <= end:
        mid = start + (end - start) // 2
        #diff = min(diff, abs(b[mid] - i))
        newDiff = abs(b[mid] - i)
        if newDiff < diff:
            diff = newDiff
            ib = b[mid]
        if i == b[mid]:
            return 0, b[mid]
        if i < b[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return diff, ib

c = [1,3,15,11,2]
d = [23, 127, 235, 19, 8]
print findSmallestDiff(c, d)
