# 2528. Maximize the Minimum Powered City
# https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution:
    def maxPower(self, stations, r, k):
        '''
        def valid(target):
            limit=k
            idx=0
            power=st.copy()
            while idx<n:
                if power[idx]>=target:
                    idx+=1
                    continue
                if power[idx]<target and limit>0:
                    if target-power[idx]>(limit):
                        return False
                    need=target-power[idx]
                    for j in range(idx,min(n,idx+r+r+1)):
                        power[j]+=need
                    limit-=need
                if power[idx]<target:
                    return False
                idx+=1
            return True
                
        start=min(stations)
        n=len(stations)
        st=stations.copy()
        s=sum(stations[:min(n,r+1)])
        st[0]=s
        for idx in range(1,n):
            s-=(stations[idx-r-1] if idx-r-1>=0 else 0)
            s+=(stations[idx+r] if idx+r<n else 0)
            st[idx]=s
        end=sum(stations)+k
        while start<=end:
            mid=(start+end)//2
            if valid(mid):
                start=mid+1
            else:
                end=mid-1
        return start-1
        '''

        def valid(target):
            curr=sum(stations[:r])
            additionalStations=k
            added=[0]*n
            for idx in range(n):
                if idx+r<n:
                    curr+=stations[idx+r]
                if curr<target:
                    needed=target-curr
                    if needed>additionalStations:
                        return False
                    additionalStations-=needed
                    added[min(n-1,idx+r)]=needed
                    curr+=needed
                if idx-r>=0:
                    curr-=(stations[idx-r]+added[idx-r])
            return True

        left=min(stations)
        right=sum(stations)+k
        n=len(stations)
        while left<=right:
            mid=(left+right)//2
            if valid(mid):
                left=mid+1
            else:
                right=mid-1
        return left-1