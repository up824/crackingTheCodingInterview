#16.5 Factorial Zeros
def factorialZeros(n):
    cnt = 0
    while n:
        n //= 5
        cnt += n
    return cnt
