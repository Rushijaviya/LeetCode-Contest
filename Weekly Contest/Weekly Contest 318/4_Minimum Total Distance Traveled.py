# 2463. Minimum Total Distance Traveled
# https://leetcode.com/problems/minimum-total-distance-traveled/

from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robot, factory):
        
        @lru_cache(None)
        def dp(i,j,k):
            if i==m:
                return 0
            if j==n:
                return float('inf')
            don=dp(i,j+1,0)
            dos=dp(i+1,j,k+1)+abs(robot[i]-factory[j][0]) if k<factory[j][1] else float('inf')
            return min(don,dos)

        m,n=len(robot),len(factory)
        robot.sort()
        factory.sort()
        return dp(0,0,0)