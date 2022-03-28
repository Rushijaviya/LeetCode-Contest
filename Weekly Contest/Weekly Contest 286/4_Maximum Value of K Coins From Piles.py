# 2218. Maximum Value of K Coins From Piles
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

# from functools import lru_cache

class Solution:
    def maxValueOfCoins(self, piles, k):
        @lru_cache(None)
        def dp(i,k):
            if i==len(piles) or k==0:
                return 0
            ans=dp(i+1,k)
            curr=0
            for j in range(min(k,len(piles[i]))):
                curr+=piles[i][j]
                ans=max(ans,curr+dp(i+1,k-j-1))
            return ans

        return dp(0,k)