#10.4 Sorted Search, No Size
def sortedSearch(target):
    if elementAt(0) == target:
        return 0
    end = 1
    while elementAt(end) <= target:
        if elementAt(end) == -1:
            return -1
        if elementAt(end) == target:
            return end
        end *= 2
    start = end / 2
    # start < target < end
    while start <= end:
        mid = start + (end - start) // 2
        midVal = elementAt(mid)
        if  midVal == -1 or midVal == target:
            return mid
        if midVal < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

nums = range(0, 1000, 2)
def elementAt(idx):
    try:
        return nums[idx]
    except IndexError:
        return -1

print sortedSearch(1340)
