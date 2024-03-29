# 2332. The Latest Time to Catch a Bus
# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/

from bisect import bisect_left

class Solution:
    def latestTimeCatchTheBus(self, buses, passengers, capacity):
        '''        
        def vaild(x):
            idx=bisect_left(passengers,x)
            i,j=0,0
            cap=[0]*m
            while i<n and j<m:
                if passengers[i]<=buses[j]:
                    cap[j]+=1
                    if cap[j]==capacity:
                        j+=1
                    i+=1
                else:
                    j+=1
            return i>idx or (i==idx and cap[-1]<capacity)

        buses.sort()
        passengers.sort()
        start=1
        end=buses[-1]
        ans=0
        m,n=len(buses),len(passengers)
        while start<=end:
            mid=(start+end)//2
            if vaild(mid):
                start=mid+1
                ans=mid
            else:
                end=mid-1
        while ans in passengers:
            ans-=1
        return ans
        '''

        buses.sort()
        passengers.sort()
        m,n=len(buses),len(passengers)
        cap=0
        j=0
        ans=0
        for i in range(m):
            while j<n and cap<capacity and passengers[j]<=buses[i]:
                if j==0 or (passengers[j]-1!=passengers[j-1]):
                    ans=passengers[j]-1
                j+=1
                cap+=1
            if cap<capacity and (j==0 or passengers[j-1]!=buses[i]):
                ans=buses[i]
            cap=0
        return ans