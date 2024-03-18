# 2708. Maximum Strength of a Group
# https://leetcode.com/problems/maximum-strength-of-a-group/

class Solution:
    def maxStrength(self, nums):
        '''
        @lru_cache(None)
        def dp(idx,value,taken):
            if idx==n:
                if taken:
                    nonlocal ans
                    ans=max(ans,value)
                return
            dp(idx+1,value,taken)
            dp(idx+1,value*nums[idx],1)

        n=len(nums)
        ans=max(nums)
        dp(0,1,0)
        return ans
        '''

        left=[i for i in nums if i<0]
        right=[i for i in nums if i>0]
        if not left and not right and 0 in nums:
            return 0
        if not right and len(left)==1:
            if 0 in nums:
                return 0
            return left[0]
        ans=reduce(lambda x,y:x*y,right) if right else 1
        left.sort()
        for idx in range(1,len(left),2):
            ans*=left[idx]
            ans*=left[idx-1]
        return ans