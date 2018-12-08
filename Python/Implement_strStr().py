class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = 0
        is_find = False

        while index < len(haystack)-len(needle)+1 and is_find != True:
            print(index)
            if haystack[index:(index + len(needle))] == needle:
                is_find = True
            else:
                index += 1

        if is_find == False:
            if haystack == needle:
                return 0
            else:
                return -1
        else:
            return index