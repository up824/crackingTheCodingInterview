#10.5 Sparse Search
def sparseSearch(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if not nums[mid]:
            # search the valid mid
            left, right = mid - 1, mid + 1
            while left >= start or right <= end:
                if left >= start and nums[left]:
                    mid = left
                    break
                if right <= end and nums[right]:
                    mid = right
                    break
                left -= 1
                right += 1
        if not nums[mid]:
            return -1

        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1

nums = [0] * 1000
for i in xrange(0, 1000, 3):
    nums[i] = i//2
print nums
print sparseSearch(nums, 192)
