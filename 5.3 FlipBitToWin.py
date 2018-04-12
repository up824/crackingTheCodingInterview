#5.3 FlipBitToWin
def flipBitToWin(n):
    i = 1
    curr = 0
    prev = 0
    res = 0
    while i < 33:
        if n & i:
            prev += 1
            curr += 1
        else:
            curr = prev + 1
            prev = 0
        res = max(res, curr)
        i += 1
    return res
