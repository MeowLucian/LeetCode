class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str=str(x)
        x_str_inv=x_str[::-1]

        if x>0:
            x_new=int(x_str_inv)
        if x<0:
            x_new=int('-' + x_str_inv[0:len(x_str_inv)-1:1])
        if x==0:
            x_new=0
        
        if x_new<=2**31-1 and x_new>=-2**31:
            return x_new
        else:
            return 0