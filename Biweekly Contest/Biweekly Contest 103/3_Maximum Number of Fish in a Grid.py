# 2658. Maximum Number of Fish in a Grid
# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid):
        '''
        def bfs(r,c):
            queue=[(r,c)]
            visited.add((r,c))
            res=0
            while queue:
                i,j=queue.pop(0)
                res+=grid[i][j]
                for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
                    if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y] and (i+x,j+y) not in visited:
                        visited.add((i+x,j+y))
                        queue.append((i+x,j+y))
            return res

        m,n=len(grid),len(grid[0])
        ans=0
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visited:
                    ans=max(ans,bfs(i,j))
        return ans
        '''

        def dfs(r,c):
            visited.add((r,c))
            res=grid[r][c]
            for x,y in [(-1,0),(0,-1),(0,1),(1,0)]:
                if 0<=r+x<m and 0<=c+y<n and grid[r+x][c+y] and (r+x,c+y) not in visited:
                    res+=dfs(r+x,c+y)
            return res
        
        m,n=len(grid),len(grid[0])
        ans=0
        visited=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i,j) not in visited:
                    ans=max(ans,dfs(i,j))
        return ans