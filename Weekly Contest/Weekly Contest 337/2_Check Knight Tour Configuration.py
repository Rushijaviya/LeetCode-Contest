# 2596. Check Knight Tour Configuration
# https://leetcode.com/problems/check-knight-tour-configuration/

class Solution:
    def checkValidGrid(self, grid):
        '''
        if grid[0][0]!=0:
            return False
        n=len(grid)
        d={}
        for i in range(n):
            for j in range(n):
                d[grid[i][j]]=(i,j)
        curr_pos=0
        move={(2,1),(2,-1),(1,2),(-1,2),(-2,1),(-2,-1),(1,-2),(-1,-2)}
        while curr_pos<(n*n)-1:
            possible_way=[(d[curr_pos][0]+i,d[curr_pos][1]+j) for i,j in move]
            if d[curr_pos+1] not in possible_way:
                return False
            curr_pos+=1
        return True
        '''

        if grid[0][0]!=0:
            return False
        n=len(grid)
        d={}
        for i in range(n):
            for j in range(n):
                d[grid[i][j]]=(i,j)
        curr_pos=0
        while curr_pos<(n*n)-1:
            prev_row,prev_col=d[curr_pos]
            next_row,next_col=d[curr_pos+1]
            if abs((next_col-prev_col)*(next_row-prev_row))!=2:
                return False
            curr_pos+=1
        return True