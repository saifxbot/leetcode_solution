class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # Store number -> index

        for i, num in enumerate(nums): # Enumerate gives us both index and value
            complement = target - num
            if complement in seen:
                return [seen[complement], i]  # Found the pair
            seen[num] = i  # Remember this number
