# 2427. Number of Common Factors
# https://leetcode.com/problems/number-of-common-factors/

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        '''
        ans=1
        for i in range(2,min(a,b)+1):
            if a%i==0 and b%i==0:
                ans+=1
        return ans
        '''

        return sum(a%i==0 and b%i==0 for i in range(1,min(a,b)+1))