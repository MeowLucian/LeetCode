class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        find = False
        while index < len(nums) and find == False:
            if target > nums[index]:
                index += 1
            else :
                find = True
        return index