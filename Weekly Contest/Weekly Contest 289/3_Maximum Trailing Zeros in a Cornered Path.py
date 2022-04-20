# 2245. Maximum Trailing Zeros in a Cornered Path
# https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

class Solution:
    def maxTrailingZeros(self, grid):
        n,m = len(grid),len(grid[0])
        res = 0
        
        def factors(x,f):
            res = 0
            while x%f == 0:
                x//=f
                res+=1
            return res
        
        def pre_sum(lst):
            pre = [(0,0)]
            for a,b in lst:
                pre.append((pre[-1][0]+a,pre[-1][1]+b))
            return pre
        
        for i in range(n):
            for j in range(m):
                grid[i][j] = factors(grid[i][j],2),factors(grid[i][j],5)
        
        rows = [pre_sum(row) for row in grid]
        cols = [pre_sum([grid[i][j] for i in range(n)]) for j in range(m)]

        for i in range(n):
            for j in range(m):
                left_row, upper_col = rows[i][j], cols[j][i]
                right_row = rows[i][-1][0] - rows[i][j+1][0],rows[i][-1][1] - rows[i][j+1][1]
                lower_col = cols[j][-1][0] -cols[j][i+1][0],cols[j][-1][1] -cols[j][i+1][1]
                x0,y0 = grid[i][j]
                for x1,y1 in [left_row,right_row]:
                    for x2,y2 in [lower_col,upper_col]:
                        res = max(res,min(x0+x1+x2,y0+y1+y2))
        return res