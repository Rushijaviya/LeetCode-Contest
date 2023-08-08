# 2617. Minimum Number of Visited Cells in a Grid
# https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/

from sortedcontainers import SortedList

class Solution:
    def minimumVisitedCells(self, grid):
        m,n=len(grid),len(grid[0])
        s1=[SortedList(range(n)) for _ in range(m)]
        s2=[SortedList(range(m)) for _ in range(n)]
        queue=[(0,0,1)]
        while queue:
            i,j,d=queue.pop(0)
            if i==m-1 and j==n-1:
                return d
            for k in list(s1[i].irange(j+1,min(n,j+1+grid[i][j])-1)):
                queue.append((i,k,d+1))
                s1[i].remove(k)
                s2[k].remove(i)
            for k in list(s2[j].irange(i+1,min(m,i+1+grid[i][j])-1)):
                queue.append((k,j,d+1))
                s1[k].remove(j)
                s2[j].remove(k)
        return -1