# 2577. Minimum Time to Visit a Cell In a Grid
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

from heapq import heappop, heappush

class Solution:
    def minimumTime(self, grid):
        '''
        # TLE
        @lru_cache(None)
        def dp(i,j,timer):
            if i==m-1 and j==n-1:
                return 1+timer
            temp=float('inf')
            for x,y in d:
                if 0<=i+x<m and 0<=j+y<n and timer<=grid[i+x][j+y]:
                    temp=min(temp,dp(i+x,j+y,1+timer))
            return temp
            
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        if grid[0][0]!=0:
            return -1
        m,n=len(grid),len(grid[0])
        x=dp(0,0,1)
        return x if x!=float('inf') else -1
        '''

        if grid[0][1]>1 and grid[1][0]>1:
            return -1
        m,n=len(grid),len(grid[0])
        queue=[(0,0,0)]
        d=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=set()
        while queue:
            time,row,col=heappop(queue)
            if row==m-1 and col==n-1:
                return time
            if (row,col) in visited:
                continue
            visited.add((row,col))
            for x,y in d:
                if 0<=row+x<m and 0<=col+y<n and (row+x,col+y) not in visited:
                    wait=(grid[row+x][col+y]-time)%2==0
                    heappush(queue,(max(1+time,grid[row+x][col+y]+wait),row+x,col+y))