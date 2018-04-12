#5.7 Pairwise Swap
def pairwiseSwap(n):
    return ((0x55555555 & n) << 1) | ((0xAAAAAAAA & n) >> 1)
