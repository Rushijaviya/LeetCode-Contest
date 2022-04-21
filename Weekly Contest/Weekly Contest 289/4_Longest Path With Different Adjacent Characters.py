# 2246. Longest Path With Different Adjacent Characters
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

from heapq import nlargest

class Solution:
    def longestPath(self, parent, s):
        n=len(parent)
        child=[[] for _ in range(n)]
        
        for i,j in enumerate(parent):
            if j>=0:
                child[j].append(i)
        
        res=[0]
        
        def dfs(i):
            candi=[0]
            for j in child[i]:
                cur=dfs(j)
                if s[i]!=s[j]:
                    candi.append(cur)
            candi=nlargest(2,candi)
            res[0]=max(res[0],sum(candi)+1)
            return max(candi)+1
        
        dfs(0)
        return res[0]