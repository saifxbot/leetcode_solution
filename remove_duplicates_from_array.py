class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:                    # Check if the list is empty
            return 0

                                        # pointer for the position of the next unique element
        k = 1  

        for i in range(1, len(nums)):   # search for unique elements
            if nums[i] != nums[i - 1]:  # found a new unique number
                nums[k] = nums[i]       # position of the next unique element
                k += 1

        return k
