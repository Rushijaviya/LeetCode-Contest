# 2493. Divide Nodes Into the Maximum Number of Groups
# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

class Solution:
    def magnificentSets(self, n, edges):
        def dfs(node):
            if color[node]==-1:
                color[node]=0
            component[node]=comp
            for nei in adj_list[node]:
                if color[nei]==-1:
                    color[nei]=1-color[node]
                    if not dfs(nei):
                        return False
                elif color[nei]==color[node]:
                    return False
            return True

        def finddepth(source):
            queue=[source]
            visited=set()
            visited.add(source)
            temp=0
            while queue:
                t=len(queue)
                for _ in range(t):
                    node=queue.pop(0)                    
                    for nei in adj_list[node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                temp+=1
            return temp

        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i-1].append(j-1)
            adj_list[j-1].append(i-1)
        comp=1
        component=[0]*n
        color=[-1]*n
        for i in range(n):
            if color[i]==-1:
                if not dfs(i):
                    return -1
                comp+=1
        ans=[0]*n
        for i in range(n):
            ans[component[i]]=max(ans[component[i]],finddepth(i))
        return sum(ans)
        
        '''
        def bfs(source):
            distance[source][source]=0
            visited=set()
            queue=[source]
            visited.add(source)
            while queue:
                node=queue.pop(0)
                for nei in adj_list[node]:
                    if distance[source][nei]>distance[source][node]+1:
                        distance[source][nei]=distance[source][node]+1
                        queue.append(nei)

        def dfs(node):
            if color[node]==-1:
                color[node]=0
            path.append(node)
            for nei in adj_list[node]:
                if color[nei]==-1:
                    color[nei]=1-color[node]
                    if not dfs(nei):
                        return False
                elif color[nei]==color[node]:
                    return False
            return True

        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i-1].append(j-1)
            adj_list[j-1].append(i-1)
        color=[-1]*n
        ans=0
        distance=[[float('inf')]*n for _ in range(n)]
        for i in range(n):
            bfs(i)
        for i in range(n):
            if color[i]==-1:
                path=[]
                if not dfs(i):
                    return -1
                temp=0
                for x in path:
                    for y in path:
                        temp=max(temp,distance[x][y])
                ans+=(temp+1)
        return ans
        '''