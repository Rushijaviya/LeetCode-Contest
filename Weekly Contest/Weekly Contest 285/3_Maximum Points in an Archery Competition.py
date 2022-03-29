# 2212. Maximum Points in an Archery Competition
# https://leetcode.com/problems/maximum-points-in-an-archery-competition/

from functools import lru_cache


class Solution:
    def maximumBobPoints(self, numArrows, aliceArrows):
        @lru_cache(None)
        def dp(k,numArrows):
            if k==12 or numArrows<=0:
                return 0

            ans=dp(k+1,numArrows)
            if numArrows>aliceArrows[k]:
                ans=max(ans,dp(k+1,numArrows-(aliceArrows[k]+1))+k)
            return ans

        ans=[0]*12
        remainBobArrows=numArrows
        for k in range(12):
            if dp(k,numArrows)!=dp(k+1,numArrows):
                ans[k]=aliceArrows[k]+1
                numArrows-=ans[k]
                remainBobArrows-=ans[k]
        ans[0]+=remainBobArrows
        return ans