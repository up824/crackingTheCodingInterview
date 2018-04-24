#10.7 Missing Int
"""
1. 1gb mem
1gb mem
8b bits
use 8b bits represent 4b integers: 1 means yes, 0 means no
use bit address

scan first bit that is 0


2. 10m mem
 2 pass
 10mbyes -> 80m bits -> 80m int
 positive number = 2**31 - 1 = 2b int
 need 2b / 80m = 200 / 8 = 25 blocks
 1 - find the missing range using block in mem(suppose 1k blocks, then block 0 represents 0 - 999)
 2 - use bit vector(BV) to find the exact interger
"""
