# 2192. All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n, edges):
        
        def dfs(pre,child):
            for j in adj_list[child]:
                if ans[j] and ans[j][-1]==pre:
                    continue
                ans[j].append(pre)
                dfs(pre,j)

        
        adj_list=[[] for _ in range(n)]
        for i in edges:
            adj_list[i[0]].append(i[1])
        ans=[[] for _ in range(n)]
        for i in range(n):
            dfs(i,i)
        return ans 