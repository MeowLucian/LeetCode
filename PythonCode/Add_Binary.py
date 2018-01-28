class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum_list = list(str(int(a)+int(b)))

        for index in range(-1,-len(sum_list),-1):
            is_add = int(int(sum_list[index]) / 2)
            sum_list[index-1] = str(int(sum_list[index-1]) + is_add)
            sum_list[index] = str(int(sum_list[index]) % 2)

        if int(int(sum_list[0]) / 2) == 1:
            sum_list[0] = str(int(sum_list[0]) % 2)
            sum_list = ["1"] + sum_list

        sum_str = ''.join(sum_list)

        return sum_str