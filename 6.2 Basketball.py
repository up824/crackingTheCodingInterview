# 6.2 Basketball
def basketball(p):
    # p: float
    # return "Game 1" or "Game 2"
    p1 = p
    p2 = (1 - p) * p ** 2 * 3 + p ** 3

    if p1 > p2:
        return "Game 1"
    else:
        return "Game 2"
