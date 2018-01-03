class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x>=0:
            x_str=str(x)
            left=0
            right=len(x_str)-1
            Find=True
            while left<=right:
                if x_str[left]==x_str[right]:
                    left=left+1
                    right=right-1
                else:    
                    Find=False
                    break
            if Find==True:
                return True
            else:
                return False
        else:
            return False