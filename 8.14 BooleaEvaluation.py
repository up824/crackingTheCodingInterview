# 8.14 Boolean Evaluation
import collections
def countEval(s, result):
    return _dfs(s, "1" if result else "0", {})

def _dfs(s, result, memo):
    if not s :
        return 0
    if len(s) == 1:
        return 1 if s == result else 0

    if (s, result) in memo:
        return memo[(s, result)]

    ways = 0
    for i in xrange(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1:]
        leftTrue = _dfs(left, "1", memo)
        leftFalse = _dfs(left, "0", memo)
        rightTrue = _dfs(right, "1", memo)
        rightFalse = _dfs(right, "0", memo)
        total = (leftTrue + leftFalse) * (rightTrue + rightFalse)
        totalTrue = 0
        if c == "^":
            totalTrue = leftTrue * rightFalse + leftFalse * rightTrue
        elif c == "&":
            totalTrue = leftTrue * rightTrue
        elif c == "|":
            totalTrue = leftTrue * rightTrue + leftFalse * rightTrue + leftTrue * rightFalse

        subWays = totalTrue if result == "1" else total - totalTrue
        ways += subWays
    memo[(s, result)] = ways
    return ways





def booleanEvaluation(expression, result):
    #0, 1, &, |, ^
    mem = collections.defaultdict(int)
    result = "1" if result else "0"
    return dfs(expression, result, mem)

def dfs(exp, target, mem):
    # return valid num
    print exp, target, mem
    if len(exp) == 1:
        if  exp in target:
            return 1
        return 0

    #if (exp, target) in mem:
    #    return mem[(exp, target)]

    ways = 0
    for i in xrange(0, len(exp), 2):
        curr = eval(exp[:i + 1])
        curr = "1" if curr else "0"
        print "curr ", exp[:i + 1],  curr," remain ", exp[i + 1:], " target ", target, " ways ", ways
        if i == len(exp) - 1: # last one
            if curr == target:
                ways += 1
        else:
            symbol = exp[i + 1]
            newTarget = getNewTarget(curr, target, symbol)
            if not newTarget:
                continue
            ways += dfs(exp[i + 2:], newTarget, mem)
    mem[exp, target] = ways
    return ways

def getNewTarget(curr, target, symbol):

    if target == "10":
        return "10"

    if symbol == "&":
        if target == "1":
            if curr == "1":
                return "1"
            return ""
        elif target == "0":
            if curr == "1":
                return "0"
            return "10"

    elif symbol == "|":
        if target == "1":
            if curr == "1":
                return "10"
            else:
                return "1"
        else:
            if curr == "1":
                return ""
            else:
                return "0"
    elif symbol == "^":
        if target == "1":
            return "1" if curr == "0" else "0"
        else:
            return curr

print countEval("1^0|0|1", False)
print countEval("0&0&0&1^1|0", True)
