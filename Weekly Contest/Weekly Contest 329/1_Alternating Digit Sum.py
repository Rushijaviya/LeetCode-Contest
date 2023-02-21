# 2544. Alternating Digit Sum
# https://leetcode.com/problems/alternating-digit-sum/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        '''
        l=list(map(int,list(str(n))))
        ans=0
        sign=1
        for i in l:
            ans+=(i*sign)
            sign*=(-1)
        return ans
        '''

        ans=0
        sign=1
        while n:
            sign*=(-1)
            ans+=((n%10)*sign)
            n//=10
        return sign*ans