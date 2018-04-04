# 1.8 Zero Matrix zero col and row in a m*n matrix  if an element is Zero
def zeroMatrix(matrix):
    # matrix is list(list(int))
    # return void
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    col0, row0 = False, False
    # check row 0 and col 0
    for i in xrange(n):
        if matrix[0][i] == 0:
            row0 = True
            break
    for i in xrange(m):
        if matrix[i][0] == 0:
            col0 = True
            break
    # use row 0 to store col info, use col 0 to store row info
    for i in xrange(1, m):
        for j in xrange(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    #zero the matrix based on col0 and row0 info
    for i in xrange(1, n):
        if matrix[0][i] == 0:
            for j in xrange(1, m):
                matrix[j][i] = 0
    for i in xrange(1, m):
        if matrix[i][0] == 0:
            for j in xrange(1, n):
                matrix[i][j] = 0
    if row0:
        for i in xrange(n):
            matrix[0][i] = 0
    if col0:
        for i in xrange(m):
            matrix[i][0] = 0

import unittest
class Test(unittest.TestCase):
    def test_zeroMatrix(self):
        cases = [([[1, 1, 1, 0], [1, 0, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]])]
        for inMatrix, outMatrix in cases:
            zeroMatrix(inMatrix)
            self.assertEqual(inMatrix, outMatrix)

if __name__ == '__main__':
    unittest.main()
