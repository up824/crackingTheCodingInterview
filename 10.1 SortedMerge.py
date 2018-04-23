#10.1 Sorted Merge
def sortedMerge(a,  b):
    m, n = len(a), len(b)
    pa, pb = m - n - 1, n - 1
    for i in xrange(m - 1, -1, -1):

        if pb < 0 or (pa >= 0 and a[pa] > b[pb]):
            a[i] = a[pa]
            pa -= 1
        else: # pb >= 0 and (pa < 0 or a[pa] <= b[pb])
            a[i] = b[pb]
            pb -= 1

a = [1,5,6,98,1241,0,0,0,0]
b = [4, 66, 123, 424]
sortedMerge(a, b)
print a
