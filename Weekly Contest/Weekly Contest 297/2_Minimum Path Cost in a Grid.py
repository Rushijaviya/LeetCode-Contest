# 2304. Minimum Path Cost in a Grid
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

import heapq

class Solution:
    def minPathCost(self, grid, moveCost):
        # Dijkstra
        queue=[]
        ans=float('inf')
        m,n=len(grid),len(grid[0])
        visited=[[float('inf')]*n for _ in range(m)]
        for i in range(n):
            visited[0][i]=grid[0][i]
            heapq.heappush(queue,(0,i,visited[0][i]))
        
        while queue:
            i,j,cost=heapq.heappop(queue)
            if cost>visited[i][j]:
                continue
            if i==m-1:
                ans=min(ans,cost)
            else:
                for newj in range(n):
                    newcost=cost+grid[i+1][newj]+moveCost[grid[i][j]][newj]
                    if newcost<visited[i+1][newj]:
                        visited[i+1][newj]=newcost
                        heapq.heappush(queue,(i+1,newj,newcost))
        return ans
        
        '''
        # DP
        m,n=len(grid),len(grid[0])
        dp=[[float('inf')]*n for _ in range(m)]
        dp[0]=grid[0]
        for i in range(1,m):
            for j in range(n):
                for k in range(n):
                    dp[i][k]=min(dp[i][k],dp[i-1][j]+grid[i][k]+moveCost[grid[i-1][j]][k])
        return min(dp[-1])
        '''

        '''
        # DP - Memory optimization
        m,n=len(grid),len(grid[0])
        dp=grid[0]
        for i in range(1,m):
            curr=[float('inf')]*n
            for j in range(n):
                for k in range(n):
                    curr[k]=min(curr[k],dp[j]+grid[i][k]+moveCost[grid[i-1][j]][k])
            dp=curr
        return min(dp)
        '''

        '''
        # TLE - Dijkstra
        m,n=len(grid),len(grid[0])
        adj_list=[[] for _ in range(m*n)]
        for i in range(1,m):
            for j in range(n):
                for k in range(n):
                    adj_list[grid[i-1][k]].append((grid[i][j],moveCost[grid[i-1][k]][j]+grid[i-1][k]))
        
        ans=float('inf')
        for source in grid[0]:
            distance=[float('inf')]*(m*n)
            distance[source]=0
            queue=[(0,source)]

            while queue:
                dis,node=heapq.heappop(queue)
                for i,j in adj_list[node]:
                    if dis+j<distance[i]:
                        distance[i]=dis+j
                        heapq.heappush(queue,(distance[i],i))
            
            for i in grid[-1]:
                ans=min(ans,distance[i]+i)
        return ans
        '''