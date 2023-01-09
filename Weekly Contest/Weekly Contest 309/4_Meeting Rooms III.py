# 2402. Meeting Rooms III
# https://leetcode.com/problems/meeting-rooms-iii/

from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def mostBooked(self, n, meetings):
        '''
        meetings.sort()
        d=defaultdict(int)
        time=[0]*n
        for i,j in meetings:
            mintime=float('inf')
            for k in range(n):
                mintime=min(mintime,time[k])
                if time[k]<=i:
                    time[k]=j
                    d[k]+=1
                    break
            else:
                for k in range(n):
                    if time[k]==mintime:
                        time[k]+=(j-i)
                        d[k]+=1
                        break
        l=[[i,j] for i,j in d.items()]
        l.sort(key=lambda x:-x[1])
        return l[0][0]
        '''
        
        '''
        meetings.sort()
        count=[0]*n
        time=[0]*n
        idx=0
        for i,j in meetings:
            minindex=0
            for k in range(n):
                if time[k]<time[minindex]:
                    minindex=k
                if time[k]<=i:
                    time[k]=j
                    count[k]+=1
                    if count[k]>count[idx]:
                        idx=k
                    elif count[k]==count[idx]:
                        idx=min(idx,k)
                    break
            else:
                time[minindex]+=(j-i)
                count[minindex]+=1
                if count[minindex]>count[idx]:
                    idx=minindex
                elif count[minindex]==count[idx]:
                    idx=min(idx,minindex)
        return idx
        '''

        meetings.sort()
        ongoing=[]
        available=[i for i in range(n)]
        count=[0]*n
        res=0
        for i,j in meetings:
            while ongoing and ongoing[0][0]<=i:
                _,idx=heappop(ongoing)
                heappush(available,idx)
            if available:
                idx=heappop(available)
                heappush(ongoing,(j,idx))
                count[idx]+=1
                if count[idx]>count[res]:
                    res=idx
                elif count[idx]==count[res]:
                    res=min(res,idx)
            else:
                time,idx=heappop(ongoing)
                heappush(ongoing,(time+(j-i),idx))
                count[idx]+=1
                if count[idx]>count[res]:
                    res=idx
                elif count[idx]==count[res]:
                    res=min(res,idx)
        return res