# 2482. Difference Between Ones and Zeros in Row and Column
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution:
    def onesMinusZeros(self, grid):
        '''
        m,n=len(grid),len(grid[0])
        zero_row,zero_col=[0]*m,[0]*n
        one_row,one_col=[0]*m,[0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    one_row[i]+=1
                    one_col[j]+=1
                else:
                    zero_row[i]+=1
                    zero_col[j]+=1
        for i in range(m):
            for j in range(n):
                grid[i][j]=one_row[i]+one_col[j]-zero_row[i]-zero_col[j]
        return grid
        '''

        m,n=len(grid),len(grid[0])
        one_row=[0]*m
        one_col=[0]*n
        for i,val in enumerate(grid):
            x=val.count(1)
            one_row[i]=x-(n-x)
        for i,val in enumerate(zip(*grid)):
            x=val.count(1)
            one_col[i]=x-(m-x)
        for i in range(m):
            for j in range(n):
                grid[i][j]=one_row[i]+one_col[j]
        return grid