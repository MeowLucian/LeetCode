class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        try:
            split_str = s.split()
            return len(split_str[-1])
        except:
            return 0