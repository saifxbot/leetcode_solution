class Solution(object):
    def twoSum(self, nums, target):
        # Go through each number
        for i in range(len(nums)):
            # Check the numbers after nums[i]
            for j in range(i + 1, len(nums)):
                # If they add up to target
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return the indices
                

                