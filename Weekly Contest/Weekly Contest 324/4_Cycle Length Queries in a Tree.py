# 2509. Cycle Length Queries in a Tree
# https://leetcode.com/problems/cycle-length-queries-in-a-tree/

from math import log2

class Solution:
    def cycleLengthQueries(self, n, queries):
        ans=[]
        for i,j in queries:
            temp=0
            while i!=j:
                if i>j:
                    i//=2
                else:
                    j//=2
                temp+=1
            ans.append(1+temp)
        return ans
        
        '''
        ans=[]
        for i,j in queries:
            depth_i=int(log2(i))
            depth_j=int(log2(j))

            for _ in range(depth_i-depth_j):
                i//=2
            for _ in range(depth_j-depth_i):
                j//=2
            while i!=j:
                if i>j:
                    i//=2
                else:
                    j//=2
            depth_lca=int(log2(i))
            ans.append(1+depth_i+depth_j-2*depth_lca)
        return ans
        '''