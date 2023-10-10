# 2699. Modify Graph Edge Weights
# https://leetcode.com/problems/modify-graph-edge-weights/

from heapq import heappop, heappush


class Solution:
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        def dijkstra(start,flag):
            queue=[(0,start)]
            distance=[float('inf')]*n
            parent=[-1]*n
            distance[start]=0
            while queue:
                cost,node=heappop(queue)
                if cost>distance[node]:
                    continue
                for nei,wei in adj_list[node]:
                    if wei==-1:
                        if flag:
                            continue
                        wei=1
                    if distance[nei]>distance[node]+wei:
                        distance[nei]=distance[node]+wei
                        parent[nei]=node
                        heappush(queue,(distance[nei],nei))
            return distance,parent
        
        adj_list= [[] for _ in range(n)]
        for i,j,k in edges:
            adj_list[i].append([j,k])
            adj_list[j].append([i,k])
            
        distance1,parent1=dijkstra(destination,True)
        if distance1[source]<target:
            return []
        distance2,parent2=dijkstra(source,False)
        if distance2[destination]>target:
            return []
        path=[destination]
        while path[-1]!=source:
            path.append(parent2[path[-1]])
        path=path[::-1]
        edges={(min(u,v),max(u,v)):w  for u,v,w in edges}
        total_cost=0
        for u,v in zip(path,path[1:]):
            edge=(min(u,v),max(u,v))
            if edges[edge]==-1:
                edges[edge]=max(1,target-total_cost-distance1[v])
                if edges[edge]>1:
                    break
            total_cost+=edges[edge]
        for edge,wei in edges.items():
            if wei==-1:
                edges[edge]=target+1
        return [(u,v,w) for (u,v),w in edges.items()]