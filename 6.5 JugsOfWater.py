#6.5 Jugs of Water
"""
think backwards
to get 4 quart, the final status is (4, 0)
initial status is (0, 0).
we can have intermediate status is (5, 0), (0, 3), (5, 3) ...
operations include :
    1. clean left  (0, r)
    2. clean right (l, 0)
    3. fillup left (5, r)
    4. fillup right (l, 5)
    5. fillup left with right (l, r)
        if l + r <= 5:
            (l + r, 0)
        else:
            (5, l + r - 5)
    6. fillup right with left (l, r)
        if l + r <=3 :
            (0, l + r)
        else:
            (l + r - 3, 3)
searching -> (0, 0) -> (5, 0) -> (2, 3) -> (2, 0) -> (0, 2) -> (5, 2) -> (4, 3)
so we can do bfs here to get minimum steps, and use dfs to get all solutions, check word ladder ii
"""
