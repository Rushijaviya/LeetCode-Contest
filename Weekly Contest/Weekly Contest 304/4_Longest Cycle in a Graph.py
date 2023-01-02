# 2360. Longest Cycle in a Graph
# https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges):
        '''
        # TLE
        def rec(node,per,count,visited):
            if node==per:
                return count
            if node in visited or edges[node]==-1:
                return float('-inf')
            return rec(edges[node],per,count+1,visited|set([node]))

        n=len(edges)
        ans=-1
        for i in range(n):
            if edges[i]!=-1:
                ans=max(ans,rec(edges[i],i,1,set([i])))
        return ans
        '''
        
        '''
        # kosaraju's algorithm
        def dfs(node,visited,temp):
            visited[node]=1
            if edges[node]!=-1 and not visited[edges[node]]:
                dfs(edges[node],visited,temp)
            temp.append(node)
            
        def dfs2(u,visited,temp):
            visited[u]=1
            temp.append(u)
            for v in rev[u]:
                if not visited[v]:
                    dfs2(v,visited,temp)
        
        n=len(edges)
        stack=[]
        visited=[0]*n

        for i in range(n):
            if not visited[i]:
                temp=[]
                dfs(i,visited,temp)
                stack+=temp
        
        rev=[[] for _ in range(n)]
        for i in range(n):
            if edges[i]!=-1:
                rev[edges[i]].append(i)
        
        ans=[]
        visited=[0]*n
        while stack:
            node=stack.pop()
            if not visited[node]:
                temp=[]
                dfs2(node,visited,temp)
                ans.append(temp)
        
        res=-1
        for i in ans:
            if len(i)>1:
                res=max(res,len(i))
        return res
        '''
        
        def dfs(node,path):
            if visited[node]:
                for i in range(len(path)):
                    if path[i]==node:
                        nonlocal ans
                        ans=max(ans,len(path)-i)
                        return 
            else:
                path.append(node)
                visited[node]=1
                if edges[node]!=-1:
                    dfs(edges[node],path)

        n=len(edges)
        visited=[0]*n
        ans=-1
        for i in range(n):
            if not visited[i]:
                dfs(i,[])
        return ans
        
        '''
        n=len(edges)
        visited=[0]*n
        ans=-1
        for i in range(n):
            if not visited[i]:
                d={}
                idx=i
                dist=0
                while idx!=-1:
                    if idx in d:
                        ans=max(ans,dist-d[idx])
                        break
                    if visited[idx]:
                        break
                    visited[idx]=True
                    d[idx]=dist
                    dist+=1
                    idx=edges[idx]
        return ans
        '''