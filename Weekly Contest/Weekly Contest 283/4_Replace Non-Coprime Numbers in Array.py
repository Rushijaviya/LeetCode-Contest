# 2197. Replace Non-Coprime Numbers in Array
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

from math import gcd, lcm

class Solution:
    def replaceNonCoprimes(self, nums):
        ans=[]
        for num in nums:
            ans.append(num)
            while len(ans)>1 and gcd(ans[-1],ans[-2])!=1:
                ans.append(lcm(ans.pop(),ans.pop()))
        return ans
        
        '''
        ans=[]
        for num in nums:
            while True:
                temp=gcd(num,ans[-1] if ans else 1)
                if temp==1:
                    break
                num*=ans.pop()//temp
            ans.append(num)
        return ans
        '''