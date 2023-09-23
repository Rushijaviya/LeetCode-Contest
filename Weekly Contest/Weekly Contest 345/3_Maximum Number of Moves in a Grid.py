# 2684. Maximum Number of Moves in a Grid
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

from functools import lru_cache

class Solution:
    def maxMoves(self, grid):
        @lru_cache(None)
        def dp(i,j):
            count=0
            for x,y in [(-1,1),(0,1),(1,1)]:
                if 0<=i+x<m and 0<=j+y<n and grid[i][j]<grid[i+x][j+y]:
                    count=max(count,dp(i+x,j+y)+1)
            return count

        m,n=len(grid),len(grid[0])
        return max(dp(i,0) for i in range(m))
        
        '''
        def dfs(i,j):
            count=0
            prev=grid[i][j]
            grid[i][j]=float('inf')
            for x,y in [(-1,1),(0,1),(1,1)]:
                if 0<=i+x<m and 0<=j+y<n and prev<grid[i+x][j+y]:
                    count=max(count,dfs(i+x,j+y)+1)
            return count

        m,n=len(grid),len(grid[0])
        return max(dfs(i,0) for i in range(m))
        '''