# 2352. Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/

from collections import Counter

class Solution:
    def equalPairs(self, grid):
        '''
        transpose=deepcopy(grid)
        n=len(grid)
        for i in range(n):
            for j in range(i):
                transpose[i][j],transpose[j][i]=transpose[j][i],transpose[i][j]
        ans=0
        for i in transpose:
            ans+=grid.count(i)
        return ans
        '''
        
        c=Counter(tuple(row) for row in grid)
        ans=0
        for col in zip(*grid):
            ans+=c[col]
        return ans