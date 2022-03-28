# 2209. Minimum White Tiles After Covering With Carpets
# https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

from functools import lru_cache


class Solution:
    def minimumWhiteTiles(self, floor, numCarpets, carpetLen):
        @lru_cache(None)
        def dp(i,k):
            if i<=0:
                return 0
            return min(dp(i-carpetLen,k-1) if k else 1000,dp(i-1,k)+int(floor[i-1]))
        
        return dp(len(floor),numCarpets)