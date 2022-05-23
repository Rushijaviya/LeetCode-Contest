# 2258. Escape the Spreading Fire
# https://leetcode.com/problems/escape-the-spreading-fire/

from bisect import bisect_left
import collections

class Solution:
    def maximumMinutes(self, A):
        '''
        # Method 1: BFS + Binary Search
        m, n = len(A), len(A[0])
        fires, seen = [], set()
        f = collections.deque()
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    fires.append((i, j))
                    seen.add((i, j))
                    f.append((i, j))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # If we stay for 'days' days.
        def helper(days):
            fire, seen = fires[::], set()
            
            # Let the fire spreads for 'days' days.
            while days > 0:
                newfire = []
                for i, j in fire:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 0 and (ni, nj) not in seen:
                            # If the fire reach us before we move, we fail.
                            if ni == 0 and nj == 0:
                                return False
                            seen.add((ni, nj))
                            newfire.append((ni, nj))
                fire = newfire[::]
                days -= 1

            # Then let the fire and us move by turn (fire first).
            safe = [(0, 0)]
            while safe:
                
                # Fire spreads first.
                newfire = []
                for i, j in fire:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 0 and (ni, nj) not in seen:
                            # If the fire reaches bot-right cell, if we are just one step close to bot-right cell
                            # We can still reach it, otherwise we fail. (Please refer to picture 2)
                            if ni == m - 1 and nj == n - 1:
                                if not ((m - 2, n - 1) in safe or (m - 1, n - 2) in safe):
                                    return False
                            seen.add((ni, nj))
                            newfire.append((ni, nj))
                fire = newfire[::]
                
                # We move then.
                newsafe = []
                for i, j in safe:
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        # If we can reach bot-right cell, success.
                        if ni == m - 1 and nj == n - 1:
                            return True
                        if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 0 and (ni, nj) not in seen:   
                            seen.add((ni, nj))
                            newsafe.append((ni, nj))
                safe = newsafe[::]
                
            # If there is no more cell for us to move before reaching bot-right cell, we fail.
            return False


        # check if always safe:
        while f:
            i, j = f.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 0 and (ni, nj) not in seen:
                    seen.add((ni, nj))
                    f.append((ni, nj))
        f = collections.deque([(0, 0)])
        while f:
            i, j = f.popleft()
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and A[ni][nj] == 0 and (ni, nj) not in seen:
                    if ni == m - 1 and nj == n - 1:
                        return 10 ** 9 
                    seen.add((ni, nj))
                    f.append((ni, nj))


        # Binary search to find maximum days:
        l, r = 0, 10 ** 4
        while l < r:
            mid = (l + r + 1) // 2
            if helper(mid):
                l = mid
            else:
                r = mid - 1

        return l if helper(l) else -1
        '''

        '''
        # Method 2: BFS
        m, n = len(A), len(A[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        ppl_time = [[-1] * n for _ in range(m)]
        fire_time = [[-1] * n for _ in range(m)]
        
        # BFS for people's arrival for each cell.
        ppl_front = collections.deque([(0, 0, 0)])
        while ppl_front:
            cx, cy, days = ppl_front.popleft()
            ppl_time[cx][cy] = days
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 0 and ppl_time[nx][ny] == -1:
                    ppl_front.append((nx, ny, days + 1))
        
        
        # BFS for fire's arrival for each cell.
        fire_front = collections.deque([(x, y, 0) for x in range(m) for y in range(n) if A[x][y] == 1])
        while fire_front:
            cx, cy, days = fire_front.popleft()
            fire_time[cx][cy] = days
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < m and 0 <= ny < n and A[nx][ny] == 0 and fire_time[nx][ny] == -1:
                    fire_front.append((nx, ny, days + 1))
        
        # Check the arrival days for the bottom-right cell.
        ppl_arrival = ppl_time[-1][-1]
        fire_arrival = fire_time[-1][-1]
        
        # Some edge cases.
        if ppl_arrival == -1:
            return -1
        if fire_arrival == -1:
            return 10 ** 9
        if fire_arrival < ppl_arrival:
            return -1

        # Whether we are 'followed' by fire on both two pathes toward bot-right cell.
        diff = fire_arrival - ppl_arrival
        ppl_1, ppl_2 = ppl_time[-1][-2], ppl_time[-2][-1]
        
        fire_1, fire_2 = fire_time[-1][-2], fire_time[-2][-1]
        if ppl_1 > -1 and ppl_2 > -1 and (fire_1 - ppl_1 > diff or fire_2 - ppl_2 > diff):
            return diff
        return diff - 1
        '''

        # Method 3: BFS - Lee215
        m, n = len(A), len(A[0])
        inf = 10 ** 10
        d = [[0,1],[1,0],[0,-1],[-1,0]]
        fires = [[i, j, 0] for i in range(m) for j in range(n) if A[i][j] == 1]
        A = [[inf if a < 2 else -1 for a in r] for r in A]

        def bfs(queue, seen):
            for i, j, t in queue:
                if seen[i][j] < inf: continue
                seen[i][j] = t
                for di,dj in d:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and seen[x][y] >= inf and t + 1 < A[x][y]:
                        queue.append([x, y, t + 1])
        
        def die(t):
            seen = [[inf + 10] * n for i in range(m)]
            bfs([[0, 0, t]], seen)
            return seen[-1][-1] > A[-1][-1]

        bfs(fires, A)
        A[-1][-1] += 1
        return bisect_left(range(10**9 + 1), True, key=die) - 1