# 2368. Reachable Nodes With Restrictions
# https://leetcode.com/problems/reachable-nodes-with-restrictions/

class Solution:
    def reachableNodes(self, n: int, edges, restricted) -> int:
        '''
        def dfs(node,visited,path):
            path.append(node)
            visited.add(node)
            for u in adj_list[node]:
                if u not in visited:
                    dfs(u,visited,path)
        
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        visited=set(restricted)
        path=[]
        dfs(0,visited,path)
        return len(path)
        '''

        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        visited=set(restricted)
        queue=[0]
        visited.add(0)
        count=0
        while queue:
            node=queue.pop(0)
            count+=1
            for u in adj_list[node]:
                if u not in visited:
                    queue.append(u)
                    visited.add(u)
        return count