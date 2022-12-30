# 2359. Find Closest Node to Given Two Nodes
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

class Solution:
    def closestMeetingNode(self, edges, node1, node2):
        '''
        def dijkstra(source):
            distance=[float('inf')]*n
            distance[source]=0
            queue=[(0,source)]
            while queue:
                _,node=heappop(queue)
                for nei in adj_list[node]:
                    if distance[nei]>1+distance[node]:
                        distance[nei]=1+distance[node]
                        heappush(queue,(distance[nei],nei))
            return distance
        
        n=len(edges)
        adj_list=[[] for _ in range(n)]
        for i in range(n):
            if edges[i]!=-1:
                adj_list[i].append(edges[i])
        
        dist1=dijkstra(node1)
        dist2=dijkstra(node2)
        ans=-1
        distance=float('inf')
        for i in range(n):
            if max(dist1[i],dist2[i])<distance:
                ans=i
                distance=max(dist1[i],dist2[i])
        return ans
        '''
        
        '''
        def bfs(source):
            distance=[float('inf')]*n
            distance[source]=0
            queue=[(0,source)]
            while queue:
                _,node=queue.pop(0)
                for nei in adj_list[node]:
                    if distance[nei]>1+distance[node]:
                        distance[nei]=1+distance[node]
                        queue.append((distance[nei],nei))
            return distance
        
        n=len(edges)
        adj_list=[[] for _ in range(n)]
        for i in range(n):
            if edges[i]!=-1:
                adj_list[i].append(edges[i])
        
        dist1=bfs(node1)
        dist2=bfs(node2)
        ans=-1
        distance=float('inf')
        for i in range(n):
            if max(dist1[i],dist2[i])<distance:
                ans=i
                distance=max(dist1[i],dist2[i])
        return ans
        '''

        def dfs(source,distance):
            for nei in adj_list[source]:
                if distance[nei]>1+distance[source]:
                    distance[nei]=1+distance[source]
                    dfs(nei,distance)
            return distance

        n=len(edges)
        adj_list=[[] for _ in range(n)]
        for i in range(n):
            if edges[i]!=-1:
                adj_list[i].append(edges[i])
        
        distance=[float('inf')]*n
        distance[node1]=0
        dist1=dfs(node1,distance)

        distance=[float('inf')]*n
        distance[node2]=0        
        dist2=dfs(node2,distance)
        
        ans=-1
        distance=float('inf')
        for i in range(n):
            if max(dist1[i],dist2[i])<distance:
                ans=i
                distance=max(dist1[i],dist2[i])
        return ans