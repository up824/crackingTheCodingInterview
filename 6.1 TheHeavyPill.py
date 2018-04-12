#6.1 The Heavy Pill
def theHeavyPill(nums):
    def helper(left, right):
        if left == right:
            return left
        if right - left == 1:
            # 2 bottle
            if nums[left] > nums[right]:
                return right
            return left

        mid = (right - left) / 2
        if (right - left) % 2 == 0:
            # odd
            left = sum(nums[left : mid])
            right = sum(nums[mid + 1: right + 1])
            if left == right:
                return mid
        else:
            # even
            left = sum(nums[left : mid])
            right = sum(nums[mid : right + 1])

        if left < right:
            return helper(left, mid - 1)
        else:
            return helper(mid + 1, right)

    return helper(0, len(nums) - 1)
