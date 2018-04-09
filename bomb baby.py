def answer(M, F):
    # your code here
    """
    creation fomular
    1. M = M + F
    2. F = M + F
    """
    step = 0
    m, f = int(M), int(F)
    big, small = max(m, f), min(m, f)
    while big > 0 and small > 0:
        # check if it's done
        if big == 1 and small == 1:
            return str(step)

        if big < small:
            big, small = small, big
        # one generation
        big -= small
        step += 1

    return "impossible"


import unittest
class Test(unittest.TestCase):
    def test_answer(self):
        cases = [("1", "1", "0"), ("4", "7", "4"), ("1", "2", "1"), ("2", "4", "impossible")]
        for M, F, res in cases:
            self.assertEqual(answer(M, F), res)

if __name__ == "__main__":
    unittest.main()
