class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for index in range(len(strs[0])):
            for string in strs[1:]:
                if index >= len(string) or string[index] != strs[0][index]:
                    return strs[0][:index]
        return strs[0]