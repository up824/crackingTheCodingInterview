#10.3 Search in Rotated Array
def searchInRotatedArray(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[end]:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

nums = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
target = 5
print searchInRotatedArray(nums, target)
