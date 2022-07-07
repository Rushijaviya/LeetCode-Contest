# 2317. Maximum XOR After Operations
# https://leetcode.com/problems/maximum-xor-after-operations/

from functools import reduce

class Solution:
    def maximumXOR(self, nums):
        '''
        ans=0
        for i in nums:
            ans |= i
        return ans
        '''

        return reduce(lambda x,y:x|y,nums)

        '''
        x=len(bin(max(nums)))-2
        l=[bin(i)[2:] for i in nums]
        ans=[0]*x
        idx=x-1
        while idx>=0:
            temp=0
            for i in range(len(l)):
                if len(l[i]):
                    temp|= int(l[i][-1])
                    l[i]=l[i][:-1]
            ans[idx]=str(temp)
            idx-=1
        return int("".join(ans),2)
        '''