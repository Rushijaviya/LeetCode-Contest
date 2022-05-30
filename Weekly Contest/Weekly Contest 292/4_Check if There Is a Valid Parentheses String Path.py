# 2267. Check if There Is a Valid Parentheses String Path
# https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/

from functools import lru_cache

class Solution:
    def hasValidPath(self, grid):
        row,col=len(grid),len(grid[0])
        @lru_cache(None)
        def dp(i,j,count):
            if i==row or j==col or count<0:
                return False
            count+=(1 if grid[i][j]=='(' else -1)
            if i==row-1 and j==col-1 and count==0:
                return True
            return dp(i+1,j,count) or dp(i,j+1,count)
        
        return dp(0,0,0)
        
        '''
        row,col=len(grid),len(grid[0])
        
        def solve(i,j,count):
            if i>=row or j>=col:
                return 0
            count+=(1 if grid[i][j]=='(' else -1)
            if count<0:
                return 0
            if i==row-1 and j==col-1:
                return count==0
            if dp[i][j][count]!=-1:
                return dp[i][j][count]
            dp[i][j][count]=solve(i+1,j,count) or solve(i,j+1,count)
            return dp[i][j][count]

        dp=[[[-1]*202 for _ in range(100)] for __ in range(100)]
        return solve(0,0,0)
        '''