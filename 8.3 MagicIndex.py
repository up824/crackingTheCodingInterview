# 8.3 Magic index
def magicIndex(arr):
    for i, num in enumerate(arr):
        if i == num:
            return True
    return False
