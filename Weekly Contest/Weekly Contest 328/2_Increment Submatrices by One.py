# 2536. Increment Submatrices by One
# https://leetcode.com/problems/increment-submatrices-by-one/

from itertools import accumulate

class Solution:
    def rangeAddQueries(self, n, queries):
        '''
        mat=[[0]*n for _ in range(n)]
        for a,b,c,d in queries:
            for row in range(a,c+1):
                mat[row][b]+=1
                if d+1<n:
                    mat[row][d+1]-=1
        for i in range(n):
            mat[i]=list(accumulate(mat[i]))
        return mat
        '''

        mat=[[0]*n for _ in range(n)]
        for a,b,c,d in queries:
            mat[a][b]+=1
            if d+1<n:
                mat[a][d+1]-=1
            if c+1<n:
                mat[c+1][b]-=1
            if c+1<n and d+1<n:
                mat[c+1][d+1]+=1
        for i in range(n):
            mat[i]=list(accumulate(mat[i]))
        for i in range(1,n):
            for j in range(n):
                mat[i][j]+=mat[i-1][j]
        return mat