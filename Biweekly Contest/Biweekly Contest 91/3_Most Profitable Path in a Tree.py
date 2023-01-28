# 2467. Most Profitable Path in a Tree
# https://leetcode.com/problems/most-profitable-path-in-a-tree/

from functools import lru_cache

class Solution:
    def mostProfitablePath(self, edges, bob, amount):
        '''
        def findpath(node,path,second,parent):
            if node==0:
                nonlocal ans
                ans=path+[[node,second]]
                return
            for nei in adj_list[node]:
                if nei!=parent:
                    findpath(nei,path+[[node,second]],second+1,node)
        
        @lru_cache(None)
        def dfs(node,reward,second,parent):
            if len(adj_list[node])==1 and adj_list[node][0]==parent:
                nonlocal res
                res=max(res,reward)
                return
            for nei in adj_list[node]:
                if nei!=parent:
                    if nei in d:
                        if d[nei]==second+1:
                            dfs(nei,reward+(amount[nei]//2),second+1,node)
                        elif d[nei]<second+1:
                            dfs(nei,reward,second+1,node)
                        else:
                            dfs(nei,reward+amount[nei],second+1,node)
                    else:
                        dfs(nei,reward+amount[nei],second+1,node)

        n=len(amount)
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=[]
        findpath(bob,[],0,-1)
        d={}
        for i,j in ans:
            d[i]=j
        res=float('-inf')
        dfs(0,amount[0],0,-1)
        return res
        '''

        def dfs(node,parent,distance):
            dis[node]=distance
            par[node]=parent
            for nei in adj_list[node]:
                if nei!=parent:
                    dfs(nei,node,distance+1)

        def dfs2(node,parent,distance):
            if len(adj_list[node])==1 and adj_list[node][0]==parent:
                return distance
            temp=float('-inf')
            for nei in adj_list[node]:
                if nei!=parent:
                    temp=max(temp,dfs2(nei,node,distance+amount[nei]))
            return temp

        n=len(amount)
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        dis=[0]*n
        par=[0]*n
        dfs(0,0,0)
        curr=bob
        bob_dis=0
        while curr!=0:
            if dis[curr]>bob_dis:
                amount[curr]=0
            elif dis[curr]==bob_dis:
                amount[curr]//=2
            curr=par[curr]
            bob_dis+=1
        return dfs2(0,-1,amount[0])