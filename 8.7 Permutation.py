# 8.7 Permutation
def permutation(nums):
    path = []
    res = []
    dfs(nums, path, res)
    return res

def dfs(nums, path, res):
    if not nums:
        res.append(path)

    for i, num in enumerate(nums):
        dfs(nums[:i] + nums[i + 1:], path + [num], res)


if __name__ == "__main__":
    print permutation([1,2,3,4])
