# 2661. First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/

class Solution:
    def firstCompleteIndex(self, arr, mat):
        m,n=len(mat),len(mat[0])
        d={}
        for i in range(m):
            for j in range(n):
                d[mat[i][j]]=(i,j)
        rows=[0]*m
        cols=[0]*n
        for idx in range(len(arr)):
            r,c=d[arr[idx]]
            rows[r]+=1
            cols[c]+=1
            if rows[r]==n or cols[c]==m:
                return idx