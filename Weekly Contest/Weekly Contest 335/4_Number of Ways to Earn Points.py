# 2585. Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/

from functools import lru_cache

class Solution:
    def waysToReachTarget(self, target, types):
        @lru_cache(None)
        def dp(idx,sum):
            if sum==target:
                return 1
            if idx==n:
                return 0
            temp=0
            for j in range(types[idx][0]):
                if (sum+((j+1)*(types[idx][1])))<=target:
                    temp+=dp(idx+1,sum+((j+1)*(types[idx][1])))
            temp+=dp(idx+1,sum)
            return temp%(10**9+7)

        n=len(types)
        return dp(0,0)%(10**9+7)