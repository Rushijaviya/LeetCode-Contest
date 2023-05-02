# 2642. Design Graph With Shortest Path Calculator
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

from heapq import heappop, heappush

class Graph:

    def __init__(self, n, edges):
        self.n=n
        self.adj_list=[[] for _ in range(n)]
        for u,v,cost in edges:
            self.adj_list[u].append([v,cost])

    def addEdge(self, edge):
        for idx,(v,cost) in enumerate(self.adj_list[edge[0]]):
            if v==edge[1]:
                self.adj_list[idx][1]=min(self.adj_list[idx][1],cost)
                break
        else:
            self.adj_list[edge[0]].append([edge[1],edge[2]])

    def shortestPath(self, node1, node2):
        distance=[float('inf')]*self.n
        distance[node1]=0
        queue=[(0,node1)]
        while queue:
            dis,node=heappop(queue)
            for nei,cost in self.adj_list[node]:
                if distance[nei]>cost+dis:
                    distance[nei]=cost+dis
                    heappush(queue,(distance[nei],nei))
        return -1 if distance[node2]==float('inf') else distance[node2]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)