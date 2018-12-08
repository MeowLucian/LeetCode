class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        front = 0
        back = 1
        for _ in range(n):
            new = front + back
            front = back
            back = new
        return new