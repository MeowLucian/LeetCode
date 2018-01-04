class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and Roman_map[s[i]] > Roman_map[s[i - 1]]:
                decimal += Roman_map[s[i]] - 2 * Roman_map[s[i - 1]]
            else:
                decimal += Roman_map[s[i]]
        return decimal