#213. House Robber II

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0:
            return 0;
        elif len(nums)==1:
            return nums[0];
        else:
            return max(self.findMoney(nums,0,len(nums)-2),self.findMoney(nums,1,len(nums)-1));
    
    def findMoney(self,nums,st,end):
        included = nums[st]
        nonIn = 0
        for i in range(st+1, end):
            newWith = nonIn + nums[i];
            newWithout = max(included, nonIn);
            included = newWith; 
            nonIn = newWithout;
        
        return max(included, nonIn);
    
