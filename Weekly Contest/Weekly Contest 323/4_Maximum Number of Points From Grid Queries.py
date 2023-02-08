# 2503. Maximum Number of Points From Grid Queries
# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

from bisect import bisect_left
from collections import defaultdict
import heapq

class Solution:
    def maxPoints(self, grid, queries):
        '''
        # TLE
        def dfs(i,j,max_val,visited):
            temp=0
            for x,y in d:
                if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]<max_val and (i+x,j+y) not in visited:
                    visited.add((i+x,j+y))
                    temp+=(1+dfs(i+x,j+y,max_val,visited))
            return temp            
            
        m,n=len(grid),len(grid[0])
        ans=[]
        d={(0,1),(1,0),(0,-1),(-1,0)}
        for limit in queries:
            if grid[0][0]<limit:
                ans.append(1+dfs(0,0,limit,set([(0,0)])))
            else:
                ans.append(0)
        return ans
        '''

        m,n=len(grid),len(grid[0])
        queue=[(grid[0][0],0,0)]
        grid[0][0]=0
        d=defaultdict(int)
        curr=0
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            value,i,j=heapq.heappop(queue)
            curr=max(curr,value)
            d[curr]+=1
            for x,y in direction:
                if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]:
                    heapq.heappush(queue,(grid[i+x][j+y],i+x,j+y))
                    grid[i+x][j+y]=0
        
        l=[[i,j] for i,j in d.items()]
        l.sort()
        for idx in range(1,len(l)):
            l[idx][1]+=l[idx-1][1]
        ans=[]
        for q in queries:
            idx=bisect_left(l,[q,0])
            if not idx:
                ans.append(0)
            else:
                ans.append(l[idx-1][1])
        return ans

        '''
        m,n=len(grid),len(grid[0])
        queue=[(grid[0][0],0,0)]
        grid[0][0]=0
        l=[]
        direction=[(0,1),(1,0),(-1,0),(0,-1)]
        while queue:
            value,i,j=heapq.heappop(queue)
            l.append(value)
            for x,y in direction:
                if 0<=i+x<m and 0<=j+y<n and grid[i+x][j+y]:
                    heapq.heappush(queue,(grid[i+x][j+y],i+x,j+y))
                    grid[i+x][j+y]=0
        
        max_val=l[0]
        for i in range(1,len(l)):
            max_val=max(max_val,l[i])
            l[i]=max_val
        ans=[]
        for q in queries:
            idx=bisect_left(l,q)
            ans.append(idx)
        return ans
        '''