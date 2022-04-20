class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carr = 1;
        test = 23;
        # print(len(str(test)))
        digits.reverse()
        print(digits)

        for i in range(len(digits)):
        
            # print(digits[i]);
            sum = digits[i]+carr;
            if(self.countDig(sum)>1):
                carr = 1;
            else:
                carr =0;
            digits[i]=sum%10;
            print(digits[i]);
        res = digits.reverse()
        print(res);
        return res
    
    def countDig(self, num):
        count = 0
        while num != 0:
            num//= 10
            count += 1;
        return count;
