class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(len(nums)-1):
            search = target-nums[index]
            search_list = nums[index+1:len(nums)]
            if search in search_list:
               index2 = search_list.index(search)+index+1
               break
        return [index, index2]