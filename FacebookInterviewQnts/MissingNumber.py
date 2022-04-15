#268. Missing Number
#https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ms = 0;i=0
        nums.sort();
        #print(nums)
        while i<len(nums):
            if(i!=nums[i]):
                ms=i;
                return ms;
            i+=1
        return len(nums);
                
