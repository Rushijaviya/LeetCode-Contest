# 2532. Time to Cross a Bridge
# https://leetcode.com/problems/time-to-cross-a-bridge/

from heapq import heappush,heappop

class Solution:
    def findCrossingTime(self, n: int, k: int, time):
        l,ll=[],[]
        r,rr=[],[]
        ans=currtime=0
        for idx,(a,b,c,d) in enumerate(time):
            heappush(ll,(-(a+c),-idx))
        while n or r or rr:
            if (not rr) and (not r or r[0][0]>currtime) and ((not n) or ((not ll) and (not l or l[0][0]>currtime))):
                temp=float('inf')
                if n and l:
                    temp=min(temp,l[0][0])
                if r:
                    temp=min(temp,r[0][0])
                currtime=temp
            while r and r[0][0]<=currtime:
                _,idx=heappop(r)
                heappush(rr,(-(time[idx][0]+time[idx][2]),-idx))
            while l and l[0][0]<=currtime:
                _,idx=heappop(l)
                heappush(ll,(-(time[idx][0]+time[idx][2]),-idx))
            if rr:
                _,idx=heappop(rr)
                currtime+=time[-idx][2]
                if n:
                    heappush(l,(currtime+time[-idx][3],-idx))
                else:
                    ans=max(ans,currtime)
            else:
                _,idx=heappop(ll)
                currtime+=time[-idx][0]
                heappush(r,(currtime+time[-idx][1],-idx))
                n-=1
        return ans