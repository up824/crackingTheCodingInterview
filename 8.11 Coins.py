#8.11 Coins
import collections
def coins(n):
    coins  = [25, 10, 5, 1]
    mem = collections.defaultdict(int)

    return dfs(n, coins, mem)

def dfs(amount, coins, mem):
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    if not coins:
        return 0

    if (coins[0], amount) in mem:
        return mem[(coins[0], amount)]

    ways = 0
    for i in xrange(len(coins)):
        if coins[i] > amount:
            continue
        ways += dfs(amount - coins[i], coins[i:], mem)

    mem[(coins[0], amount)] = ways
    return ways

for i in xrange(199):
    print coins(i)
