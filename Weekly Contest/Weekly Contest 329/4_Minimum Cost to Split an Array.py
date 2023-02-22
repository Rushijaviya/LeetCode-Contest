# 2547. Minimum Cost to Split an Array
# https://leetcode.com/problems/minimum-cost-to-split-an-array/

from collections import defaultdict
from functools import lru_cache

class Solution:
    def minCost(self, nums, k):
        @lru_cache(None)
        def dp(idx):
            if idx==n:
                return 0
            temp=float('inf')
            for j in range(idx,n):
                curr=trimmed[idx][j]+k
                next=dp(j+1)
                temp=min(temp,curr+next)
            return temp

        n=len(nums)
        trimmed=[[0]*n for _ in range(n)]
        for i in range(n):
            d=defaultdict(int)
            count=0
            for j in range(i,n):
                if d[nums[j]]==1:
                    count+=2
                elif d[nums[j]]>1:
                    count+=1
                d[nums[j]]+=1
                trimmed[i][j]=count
        return dp(0)
        
        '''
        @lru_cache(None)
        def dp(idx):
            if idx==n:
                return 0
            ans=float('inf')
            count=0
            d=defaultdict(int)
            for j in range(idx,n):
                if d[nums[j]]==1:
                    count+=2
                elif d[nums[j]]>1:
                    count+=1
                d[nums[j]]+=1
                curr=count+k
                next=dp(j+1)
                ans=min(ans,curr+next)
            return ans
        
        n=len(nums)
        return dp(0)
        '''