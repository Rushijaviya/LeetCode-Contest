# 2680. Maximum OR
# https://leetcode.com/problems/maximum-or/

class Solution:
    def maximumOr(self, nums, k):
        '''
        @lru_cache(None)
        def dp(idx,val,used):
            if idx==n or used==k:
                for i in range(idx,n):
                    val|=nums[i]
                nonlocal ans
                ans=max(ans,val)
                return
            dp(idx+1,val|nums[idx],used)
            nums[idx]*=2
            dp(idx,val,used+1)
            nums[idx]//=2

        ans=0
        n=len(nums)
        dp(0,0,0)
        return ans        
        '''

        prefix=nums[:]
        suffix=nums[:]
        for i in range(1,len(nums)):
            prefix[i]|=prefix[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i]|=suffix[i+1]
        ans=0
        for i in range(len(nums)):
            res = nums[i]*(2**k)
            if i>0:
                res|=prefix[i-1]
            if i+1<len(nums):
                res|=suffix[i+1]
            ans=max(ans,res)
        return ans