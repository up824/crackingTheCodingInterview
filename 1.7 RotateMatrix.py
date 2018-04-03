# 1.7 Rotate Matrix
def rotateMatrix(matrix):
    '''
    0123     C840
    4567     D951
    89AB     EA62
    CDEF     FB73

    diag
    048C
    159D
    26AE
    37BF

    diag left-bot to right-top
    FB73
    EA62   ->
    D951
    C840
    '''
    def diagReverse():
        for i in xrange(m):
            for j in xrange(n - i): #WARNING not to the end
                matrix[i][j], matrix[n-j-1][m-i-1] = matrix[n-j-1][m-i-1], matrix[i][j]

    def vertReverse():
        start, end = 0, m - 1
        while start < end:
            matrix[start], matrix[end] = matrix[end], matrix[start]
            start += 1
            end -= 1

    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    diagReverse() # x = -y
    m, n = n, m
    vertReverse()

import unittest
class Test(unittest.TestCase):
    def test_rotateMatrix(self):
        cases = [([[0,1,2,3], [4,5,6,7], [8, 9, 10, 11], [12, 13, 14, 15]],
                  [[12,8,4,0], [13,9,5,1], [14, 10, 6, 2], [15, 11, 7, 3]])]
        for input, output in cases:
            rotateMatrix(input)
            self.assertEqual(input, output)

if __name__ == '__main__':
    unittest.main()
