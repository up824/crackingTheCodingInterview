# 8.8 Permutations with Dups
def permutationsWithDups(nums):
    nums.sort()
    path = []
    res = []
    dfs(nums, path, res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)
        return

    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        dfs(nums[:i] + nums[i + 1:], path + [num], res)

if __name__ == "__main__":
    print permutationsWithDups([1,1,2,3,4])
