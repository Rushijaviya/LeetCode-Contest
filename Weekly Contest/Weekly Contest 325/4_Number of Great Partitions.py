# 2518. Number of Great Partitions
# https://leetcode.com/problems/number-of-great-partitions/

from functools import lru_cache

class Solution:
    def countPartitions(self, nums, k):
        if sum(nums)<2*k:
            return 0
        
        @lru_cache(None)
        def dp(idx,sum):
            if idx==n:
                return 1
            don=dp(idx+1,sum)
            dos=0
            if nums[idx]+sum<k:
                dos=dp(idx+1,sum+nums[idx])
            return don+dos

        n=len(nums)
        x=dp(0,0)
        return ((2**n)-(2*x))%(10**9+7)
        
        '''
        @lru_cache(None)
        def dp(idx,sum1,sum2):
            if idx==n:
                return 0
            don=dp(idx+1,sum1,sum2)
            dos=dp(idx+1,sum1-nums[idx],sum2+nums[idx])+((sum1-nums[idx])>=k and (sum2+nums[idx])>=k)
            return don+dos

        n=len(nums)
        return dp(0,sum(nums),0)%(10**9+7)
        '''