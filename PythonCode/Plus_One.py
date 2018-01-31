class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        list_Add = digits
        list_Add[-1] = list_Add[-1] + 1

        for index in range(-1,-len(list_Add),-1):
            is_add = int(list_Add[index] / 10)
            list_Add[index-1] = list_Add[index-1] + is_add
            list_Add[index] = int(list_Add[index] % 10)

        if int(list_Add[0] / 10) == 1:
            list_Add[0] = int(list_Add[0] % 2) 
            list_Add = [1] + list_Add
        
        return list_Add