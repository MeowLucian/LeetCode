class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Find=False
        index=0
        while Find==False:
            try:
                if index < len(nums)-1:
                    index2_num=target-nums[index]
                    nums_without_index=nums
                    nums_without_index[index]='None' # Not use the same element twice
                    index2=nums_without_index.index(index2_num)
                    return ([index,index2])
                Find=True
            except ValueError:
                index=index+1