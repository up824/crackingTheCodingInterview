# 6.8 The Egg Drop Problem
"""
fixed range:
100/x + x - 1
-> x ~= 19

dynamic range, load balanced total steps
x + (x - 1) + (x - 2) + ... + 1 = 100
(x + 1) * x / 2 = 100
x ~= 14
so
14 + 13 + 12 + 11 + 10 + 9 ...
(13 + 1) , (12 + 2), (11 + 3) ...
"""
