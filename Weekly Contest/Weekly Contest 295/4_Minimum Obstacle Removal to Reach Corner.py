# 2290. Minimum Obstacle Removal to Reach Corner
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

from collections import deque
import heapq

class Solution:
    def minimumObstacles(self, grid):
        R, C = len(grid), len(grid[0])
        d = [(1,0),(-1,0),(0,1),(0,-1)]
        distances = [[-1] * C for _ in range(R)]
        q = deque([(0, 0, 0)])
        
        while q:
            for _ in range(len(q)):
                dist, r, c = q.popleft()
                
                for dr, dc in d:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < R and 0 <= cc < C and distances[rr][cc] == -1:
                        
                        if grid[rr][cc] == 1:
                            distances[rr][cc] = dist + 1
                            q.append((dist + 1, rr, cc))
                            
                        else:
                            distances[rr][cc] = dist
                            q.appendleft((dist, rr, cc))
                            
        return distances[R - 1][C - 1]
        
        '''
        m, n = len(grid), len(grid[0])
        q = [(0, 0, 0)]
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]

        while q:
            obs, x, y = heapq.heappop(q)
            if dist[x][y] < float('inf'): continue
            obs += grid[x][y]
            dist[x][y] = obs
            if x + 1 < m: heapq.heappush(q, (obs, x + 1, y))
            if x > 0: heapq.heappush(q, (obs, x - 1, y))
            if y + 1 < n: heapq.heappush(q, (obs, x, y + 1))
            if y > 0: heapq.heappush(q, (obs, x, y - 1))
        return dist[m - 1][n - 1]
        '''