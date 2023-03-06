# 2581. Count Number of Possible Root Nodes
# https://leetcode.com/problems/count-number-of-possible-root-nodes/

from functools import lru_cache

class Solution:
    def rootCount(self, edges, guesses, k):
        '''
        # TLE
        def createroot(idx):
            queue=[idx]
            new_adj=[[] for _ in range(n)]
            visited=set()
            visited.add(idx)
            while queue:
                node=queue.pop(0)
                for nei in adj_list[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
                        new_adj[node].append(nei)
            return new_adj
        
        n=len(edges)+1
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=0
        for i in range(n):
            temp=createroot(i)
            count=0
            for i,j in guesses:
                if j in temp[i]:
                    count+=1
            ans+=(count>=k)
        return ans
        '''

        @lru_cache(None)
        def getcountofpair(node,parent):
            count=0
            for nei in adj_list[node]:
                if nei==parent:
                    continue
                if (node,nei) in correct:
                    count+=1
                count+=getcountofpair(nei,node)
            return count

        n=len(edges)+1
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=0
        correct=set((i,j) for i,j in guesses)
        for i in range(n):
            if getcountofpair(i,-1)>=k:
                ans+=1
        return ans
    
        '''
        def dfs(node,parent):
            dp[node]=0
            for nei in adj_list[node]:
                if nei!=parent:
                    if (node,nei) in correct:
                        dp[node]+=1
                    dp[node]+=dfs(nei,node)
            return dp[node]
        
        def dfs2(node,parent):
            for nei in adj_list[node]:
                if nei!=parent:
                    dp[nei]=dp[node]-(1 if (node,nei) in correct else 0)+(1 if (nei,node) in correct else 0)
                    dfs2(nei,node)
        
        n=len(edges)+1
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        correct=set((i,j) for i,j in guesses)
        dp=[0]*(n)
        dfs(0,-1)
        dfs2(0,-1)
        return sum(i>=k for i in dp)
        '''