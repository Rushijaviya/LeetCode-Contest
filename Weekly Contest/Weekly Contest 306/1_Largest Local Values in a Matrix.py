# 2373. Largest Local Values in a Matrix
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid):
        '''
        n=len(grid)
        ans=[[-1]*(n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        ans[i][j]=max(ans[i][j],grid[x][y])
        return ans
        '''

        n=len(grid)
        ans=[[-1]*(n-2) for _ in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                ans[i-1][j-1]=max(grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1])
        return ans