# 2328. Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

from functools import lru_cache

class Solution:
    def countPaths(self, grid):
        
        '''
        # TLE
        def dfs(i,j,visited,prev):
            if not (0<=i<m and 0<=j<n and (i,j) not in visited and grid[i][j]>prev):
                return 0
            return 1+dfs(i-1,j,visited|set((i,j)),grid[i][j])+dfs(i+1,j,visited|set((i,j)),grid[i][j])+dfs(i,j+1,visited|set((i,j)),grid[i][j])+dfs(i,j-1,visited|set((i,j)),grid[i][j])

        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                ans+=dfs(i,j,set(),0)
        return ans%(10**9+7)
        '''

        @lru_cache(None)
        def dfs(i,j,prev):
            if not (0<=i<m and 0<=j<n and grid[i][j]>prev):
                return 0
            return 1+dfs(i-1,j,grid[i][j])+dfs(i+1,j,grid[i][j])+dfs(i,j-1,grid[i][j])+dfs(i,j+1,grid[i][j])

        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(m):
            for j in range(n):
                ans+=dfs(i,j,0)
        return ans%(10**9+7)