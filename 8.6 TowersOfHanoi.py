# 8.6 Towers of Hanoi
def towersOfHanoi(n, src, dest, aux):
    if n == 1:
        print src + " -> " + dest + " "
    else:
        towersOfHanoi(n - 1, src, aux, dest)
        print src + " -> " + dest + " "
        towersOfHanoi(n - 1, aux, dest, src)

towersOfHanoi(3, "A", "C", "B")
