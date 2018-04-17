# 8.3 Magic index
def magicIndex(arr):
    for i, num in enumerate(arr):
        if i == num:
            return True
    return False

def magicIndex(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == mid:
            return True
        if arr[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return False
