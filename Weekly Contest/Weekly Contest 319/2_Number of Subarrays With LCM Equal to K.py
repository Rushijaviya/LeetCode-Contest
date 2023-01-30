# 2470. Number of Subarrays With LCM Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

from collections import defaultdict
from math import lcm

class Solution:
    def subarrayLCM(self, nums, k):
        '''
        count=0
        n=len(nums)
        for i in range(n):
            curr=nums[i]
            count+=(curr==k)
            for j in range(i+1,n):
                curr=lcm(curr,nums[j])
                if curr>k:
                    break
                count+=(curr==k)
        return count
        '''

        d=defaultdict(int)
        count=0
        for num in nums:
            new=defaultdict(int)
            if k%num==0:
                d[num]+=1
                for i in d:
                    new[lcm(i,num)]+=d[i]
                count+=new[k]
            d=new
        return count