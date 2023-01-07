# 2398. Maximum Number of Robots Within Budget
# https://leetcode.com/problems/maximum-number-of-robots-within-budget/

from heapq import heappop, heappush
from itertools import accumulate

class Solution:
    def maximumRobots(self, chargeTimes, runningCosts, budget):
        def vaild(length):
            queue=[]
            for i in range(length-1):
                heappush(queue,(-chargeTimes[i],i))
            for i in range(n-length+1):
                heappush(queue,(-chargeTimes[i+length-1],i+length-1))
                val,idx=queue[0]
                while idx<i:
                    val,idx=heappop(queue)
                sum=pref[i+length-1]-(pref[i-1] if i-1>=0 else 0)
                if -val+length*sum<=budget:
                    return True
            return False

        n=len(chargeTimes)
        start=1
        end=n
        pref=list(accumulate(runningCosts))
        while start<=end:
            mid=(start+end)//2
            if vaild(mid):
                start=mid+1
            else:
                end=mid-1
        return start-1
        
        '''
        def getmax(pq,j):
            while pq and pq[0][1]<j:
                heappop(pq)
            return -pq[0][0] if pq else 0

        n=len(chargeTimes)
        j=0
        s=0
        queue=[]
        ans=0
        for i in range(n):
            s+=runningCosts[i]
            heappush(queue,(-chargeTimes[i],i))
            while s*(i-j+1)+getmax(queue,j)>budget:
                s-=runningCosts[j]
                j+=1
            ans=max(ans,i-j+1)
        return ans
        '''
        
        '''
        s=SortedList()
        j=0
        n=len(chargeTimes)
        sum=0
        ans=0
        for i in range(n):
            sum+=runningCosts[i]
            s.add(chargeTimes[i])
            while s and sum*(i-j+1)+s[-1]>budget:
                s.remove(chargeTimes[j])
                sum-=runningCosts[j]
                j+=1
            ans=max(ans,i-j+1)
        return ans
        '''
        
        '''
        n=len(chargeTimes)
        sum=0
        stack=[]
        j=0
        ans=0
        for i in range(n):
            sum+=runningCosts[i]
            while stack and chargeTimes[stack[-1]]<=chargeTimes[i]:
                stack.pop()
            stack.append(i)
            while stack and sum*(i-j+1)+chargeTimes[stack[0]]>budget:
                sum-=runningCosts[j]
                if stack[0]==j:
                    stack.pop(0)
                j+=1
            ans=max(ans,i-j+1)
        return ans
        '''