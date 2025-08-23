# binary search for O(log n) runtime
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2   # find middle index
            if nums[mid] == target:     # target found
                return mid
            elif nums[mid] < target:    # search right side
                left = mid + 1
            else:                       # search left side
                right = mid - 1

        return left   # position where target should be inserted
