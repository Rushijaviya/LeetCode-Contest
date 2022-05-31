# 2270. Number of Ways to Split Array
# https://leetcode.com/problems/number-of-ways-to-split-array/

from itertools import accumulate

class Solution:
    def waysToSplitArray(self, nums):
        pre_sum=0
        post_sum=sum(nums)
        n=len(nums)
        ans=0
        for i in range(n-1):
            pre_sum+=nums[i]
            post_sum-=nums[i]
            if pre_sum>=post_sum:
                ans+=1
        return ans
        
        '''
        nums=list(accumulate(nums))
        return sum(nums[i]>=nums[-1]-nums[i] for i in range(len(nums)-1))
        '''