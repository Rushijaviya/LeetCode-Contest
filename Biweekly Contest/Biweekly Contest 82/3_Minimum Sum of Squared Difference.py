# 2333. Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/

from collections import Counter
import heapq
from sortedcontainers import SortedDict

class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        '''
        # TLE
        n=len(nums1)
        diff=[]
        for i in range(n):
            diff.append(-abs(nums1[i]-nums2[i]))
        heapq.heapify(diff)
        k=k1+k2
        while k and diff:
            x=-heapq.heappop(diff)
            k-=1
            x-=1
            if x>0:
                heapq.heappush(diff,-x)
        return sum(i**2 for i in diff)
        '''
        
        '''
        n=len(nums1)
        diff=[]
        for i in range(n):
            diff.append(-abs(nums1[i]-nums2[i]))
        if -sum(diff)<=(k1+k2):
            return 0
        heapq.heapify(diff)
        k=k1+k2
        while k:
            x=-heapq.heappop(diff)
            gap=max(1,k//n)
            k-=gap
            x-=gap
            heapq.heappush(diff,-x)
        return sum(i**2 for i in diff)
        '''
        
        '''
        n=len(nums1)
        diff=[]
        for i in range(n):
            diff.append(abs(nums1[i]-nums2[i]))
        if sum(diff)<=(k1+k2):
            return 0
        k=k1+k2
        d=SortedDict(Counter(diff))
        while k:
            key,value=d.popitem()
            if k>=value:
                d[key-1]=d.get(key-1,0)+value
                k-=value
            else:
                d[key-1]=d.get(key-1,0)+k
                d[key]=value-k
                k=0
        ans=0
        for i in d:
            ans+=((i**2)*d[i])
        return ans
        '''
        
        '''
        n=len(nums1)
        diff=[]
        for i in range(n):
            diff.append(abs(nums1[i]-nums2[i]))
        if sum(diff)<=(k1+k2):
            return 0
        k=k1+k2
        c=Counter(diff)
        d=[[-i,c[i]] for i in c]
        heapq.heapify(d)
        while k:
            key,value=heapq.heappop(d)
            key*=(-1)
            if k>=value:
                if d and -d[0][0]==key-1:
                    d[0][1]+=value
                else:
                    heapq.heappush(d,[-(key-1),value])
                k-=value
            else:
                if d and -d[0][0]==key-1:
                    d[0][1]+=k
                    heapq.heappush(d,[-key,value-k])
                else:
                    heapq.heappush(d,[-key,value-k])
                    heapq.heappush(d,[-(key-1),k])
                k=0
        ans=0
        for i,j in d:
            ans+=((i*i)*j)
        return ans
        '''
        
        # bucket sort
        n=len(nums1)
        diff=[]
        for i in range(n):
            diff.append(abs(nums1[i]-nums2[i]))
        if sum(diff)<=k1+k2:
            return 0
        m=max(diff)
        d=[0]*(m+1)
        for i in diff:
            d[i]+=1
        k=k1+k2
        for i in range(m,0,-1):
            if d[i]>0:
                minus=min(d[i],k)
                d[i]-=minus
                k-=minus
                d[i-1]+=minus
        ans=0
        for i in range(m+1):
            ans+=(d[i]*i*i)
        return ans
        
        '''
        # Binary Search
        n=len(nums1)
        diff=[]
        for i in range(n):
            diff.append(abs(nums1[i]-nums2[i]))
        start=0
        end=100000
        extra=0
        ans=0
        k=k1+k2
        while start<end:
            mid=(start+end)//2
            ops=sum(i-mid for i in diff if i>mid)
            if ops>k:
                start=mid+1
            else:
                end=mid
                extra=k-ops
        for i in diff:
            if i<start:
                val=i
            else:
                extra-=1
                val=max(0,start-(extra>=0))
            ans+=(val*val)
        return ans
        '''