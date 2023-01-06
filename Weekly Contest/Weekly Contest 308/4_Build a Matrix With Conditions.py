# 2392. Build a Matrix With Conditions
# https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution:
    def buildMatrix(self, k, rowConditions, colConditions):
        def kahns(edges,n):
            adj_list=[[] for _ in range(n)]
            degree=[0]*n
            for i,j in edges:
                adj_list[i-1].append(j-1)
                degree[j-1]+=1
            queue=[]
            for i in range(n):
                if degree[i]==0:
                    queue.append(i)
            ans=[]
            while queue:
                node=queue.pop(0)
                ans.append(node)
                for u in adj_list[node]:
                    degree[u]-=1
                    if degree[u]==0:
                        queue.append(u)
            return ans

        row_topo=kahns(rowConditions,k)
        col_topo=kahns(colConditions,k)
        if len(row_topo)!=k or len(col_topo)!=k:
            return []

        mat=[[0]*k for _ in range(k)]
        row_idx={}
        col_idx={}
        
        for i,val in enumerate(row_topo):
            row_idx[val]=i
        for i,val in enumerate(col_topo):
            col_idx[val]=i
        
        for i in range(k):
            mat[row_idx[i]][col_idx[i]]=i+1
        return mat