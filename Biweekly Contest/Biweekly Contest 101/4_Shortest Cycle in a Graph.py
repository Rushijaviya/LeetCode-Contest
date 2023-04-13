# 2608. Shortest Cycle in a Graph
# https://leetcode.com/problems/shortest-cycle-in-a-graph/

class Solution:
    def findShortestCycle(self, n, edges):
        '''
        def bfs(source):
            queue=[(source,-1)]
            distance=[float('inf')]*n
            distance[source]=0
            while queue:
                node,parent=queue.pop(0)
                for nei in adj_list[node]:
                    if distance[nei]==float('inf'):
                        distance[nei]=distance[node]+1
                        queue.append((nei,node))
                    elif nei!=parent:
                        nonlocal ans
                        ans=min(ans,distance[nei]+distance[node]+1)

        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=float('inf')
        for i in range(n):
            bfs(i)
        return ans if ans!=float('inf') else -1
        '''

        def bfs(source):
            queue=[source]
            distance=[float('inf')]*n
            distance[source]=0
            while queue:
                node=queue.pop(0)
                for nei in adj_list[node]:
                    if distance[nei]==float('inf'):
                        distance[nei]=1+distance[node]
                        queue.append(nei)
                    elif distance[node]<=distance[nei]:
                        nonlocal ans
                        ans=min(ans,distance[nei]+distance[node]+1)
                    
        
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=float('inf')
        for i in range(n):
            bfs(i)
        return ans if ans!=float('inf') else -1