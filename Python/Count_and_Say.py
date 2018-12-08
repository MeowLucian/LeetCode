class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        record_str = "1"
        ans = "1"

        for _ in range(n-1):
            class_list = [0]
            ans = ""
            for index in range(len(record_str)):
                if record_str[class_list[-1]] != record_str[index]:
                    class_list.append(index)
                else:
                    pass
            class_list.append(index+1)

            for x in range(len(class_list)-1):
                val = record_str[class_list[x]]
                ans = ans + str(class_list[x+1]-class_list[x]) + val

            record_str = ans

        return ans