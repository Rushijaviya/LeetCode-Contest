# 2428. Maximum Sum of an Hourglass
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid):
        m,n=len(grid),len(grid[0])
        ans=0
        for i in range(m-2):
            for j in range(n-2):
                s=grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                ans=max(ans,s)
        return ans