#16.1 Number Swapper
def numberSwapper1(a, b):
    print a, b
    a = a + b
    b = a - b
    a = a - b
    print a, b

def numberSwapper2(a, b):
    print a, b
    a, b = b, a
    print a, b

def numberSwapper3(a, b):
    print a, b
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print a, b

numberSwapper1(4, 1)
numberSwapper2(4, 1)
numberSwapper3(4, 1)
