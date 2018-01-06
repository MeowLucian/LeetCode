class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {"(": ")", "[": "]", "{": "}"}
        ans = True
        stack=[]
        for i in range(len(s)):
            try:
                if brackets[s[i]]:
                    stack.append(s[i])
            except:
                try:
                    if s[i] == brackets[stack[-1]]:
                        stack.pop()
                    else:
                        ans = False
                except:
                    ans = False
        if stack != []:
            ans = False
        return ans