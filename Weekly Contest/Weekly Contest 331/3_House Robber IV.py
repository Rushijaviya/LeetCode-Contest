# 2560. House Robber IV
# https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums, k):
        '''
        # TLE
        @lru_cache(None)
        def dp(i,j,x):
            nonlocal ans
            if j==k:
                ans=min(ans,x)
                return 0
            if i==0:
                if (j+1)>=k:
                    ans=min(ans,max(x,nums[0]))
                return nums[0]
            if i==1:
                if (j+1)>=k:
                    ans=min(ans,max(x,min(nums[0],nums[1])))
                return min(nums[0],nums[1])
            return max(dp(i-1,j,x),dp(i-2,j+1,max(x,nums[i]))+nums[i])
        
        ans=float('inf')
        dp(len(nums)-1,0,float('-inf'))
        return ans
        '''

        def valid(target):
            count=0
            prev=-2
            for idx in range(n):
                if nums[idx]<=target and idx!=prev+1:
                    count+=1
                    prev=idx
            return count>=k

        start=min(nums)
        end=max(nums)
        n=len(nums)
        while start<=end:
            mid=(start+end)//2
            if valid(mid):
                end=mid-1
            else:
                start=mid+1
        return end+1