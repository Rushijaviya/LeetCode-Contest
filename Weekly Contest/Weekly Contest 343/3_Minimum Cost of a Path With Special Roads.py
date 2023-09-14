# 2662. Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

from heapq import heappop, heappush

class Solution:
    def minimumCost(self, start, target, specialRoads):
        queue=[]
        n=len(specialRoads)
        distance=[float('inf')]*n
        for i in range(n):
            dist = abs(start[0]-specialRoads[i][0])+abs(start[1]-specialRoads[i][1])+specialRoads[i][4]
            distance[i]=dist
            heappush(queue,(dist,i))
        ans=abs(start[1]-target[1])+abs(start[0]-target[0])
        while queue:
            dist,idx=heappop(queue)
            ans=min(ans,abs(target[0]-specialRoads[idx][2])+abs(target[1]-specialRoads[idx][3])+dist)
            for i in range(n):
                if distance[i]>(dist+abs(specialRoads[idx][2]-specialRoads[i][0])+abs(specialRoads[idx][3]-specialRoads[i][1])+specialRoads[i][4]):
                    distance[i]=dist+abs(specialRoads[idx][2]-specialRoads[i][0])+abs(specialRoads[idx][3]-specialRoads[i][1])+specialRoads[i][4]
                    heappush(queue,(distance[i],i))
        return ans
        
        '''
        queue=[]
        n=len(specialRoads)
        distance=[float('inf')]*n
        for i in range(n):
            dist = abs(start[0]-specialRoads[i][0])+abs(start[1]-specialRoads[i][1])+specialRoads[i][4]
            distance[i]=dist
            queue.append((dist,i))
        ans=abs(start[1]-target[1])+abs(start[0]-target[0])
        while queue:
            dist,idx=queue.pop(0)
            ans=min(ans,abs(target[0]-specialRoads[idx][2])+abs(target[1]-specialRoads[idx][3])+dist)
            for i in range(n):
                if distance[i]>(dist+abs(specialRoads[idx][2]-specialRoads[i][0])+abs(specialRoads[idx][3]-specialRoads[i][1])+specialRoads[i][4]):
                    distance[i]=dist+abs(specialRoads[idx][2]-specialRoads[i][0])+abs(specialRoads[idx][3]-specialRoads[i][1])+specialRoads[i][4]
                    queue.append((distance[i],i))
        return ans
        '''