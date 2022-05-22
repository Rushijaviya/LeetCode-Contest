# 2257. Count Unguarded Cells in the Grid
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards, walls):
        matrix=[[0]*n for _ in range(m)]
        for i,j in guards+walls:
            matrix[i][j]=2
        for i,j in guards:
            up,down,left,right=i-1,i+1,j-1,j+1
            while up>=0 and matrix[up][j]!=2:
                matrix[up][j]=1
                up-=1
            while down<m and matrix[down][j]!=2:
                matrix[down][j]=1
                down+=1
            while left>=0 and matrix[i][left]!=2:
                matrix[i][left]=1
                left-=1
            while right<n and matrix[i][right]!=2:
                matrix[i][right]=1
                right+=1
        ans=0
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    ans+=1
        return ans