# 2500. Delete Greatest Value in Each Row
# https://leetcode.com/problems/delete-greatest-value-in-each-row/

class Solution:
    def deleteGreatestValue(self, grid):
        '''
        for row in grid:
            row.sort(reverse=True)
        ans=0
        for i in range(len(grid[0])):
            temp=grid[0][i]
            for j in range(1,len(grid)):
                temp=max(temp,grid[j][i])
            ans+=temp
        return ans
        '''
        
        return sum(max(col) for col in zip(*[sorted(row) for row in grid]))
        
        '''
        ans=0
        for i in range(len(grid[0])):
            temp=0
            for j in range(len(grid)):
                t=max(grid[j])
                temp=max(temp,t)
                grid[j].remove(t)
            ans+=temp
        return ans
        '''