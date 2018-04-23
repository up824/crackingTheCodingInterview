#10.2 Group Anagram
import collections
def groupAnagram(arr):
    # input : list of string
    # output : sorted list of string
    table = collections.defaultdict(list)
    for s in arr:
        ss = tuple(sorted(s))
        table[ss].append(s)

    res = []
    for val in table.values():
        res.extend(val)

    return res


arr = ["abc", "sgffff", "bca", "ffgsff","acb","eeea","fgsfff","eeae"]
print groupAnagram(arr)
