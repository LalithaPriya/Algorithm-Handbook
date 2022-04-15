# 371. Sum of Two Integers
#https://leetcode.com/problems/sum-of-two-integers/
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while(a>0):
            a-=1;
            b+=1;
        while(a<0):
            a+=1;b-=1;
        return b;
        
