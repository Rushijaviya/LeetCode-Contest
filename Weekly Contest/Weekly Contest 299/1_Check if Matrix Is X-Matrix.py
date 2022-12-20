# 2319. Check if Matrix Is X-Matrix
# https://leetcode.com/problems/check-if-matrix-is-x-matrix/

class Solution:
    def checkXMatrix(self, grid):
        n=len(grid)
        for i in range(n):
            for j in range(n):
                if i==j or i+j+1==n:
                    if grid[i][j]==0:
                        return False
                else:
                    if grid[i][j]:
                        return False
        return True