# 2338. Count the Number of Ideal Arrays
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

from functools import lru_cache
from math import comb

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        '''
        # TLE
        d={}
        d[1]=[i+1 for i in range(maxValue)]
        for i in range(2,maxValue+1):
            j=i
            d[i]=[]
            c=2
            while j<=maxValue:
                d[i].append(j)
                j=c*i
                c+=1
        ans=0
        for i in d:
            prev=d[i]
            for _ in range(n-2):
                next=[]
                for k in prev:
                    next+=d[k]
                prev=next.copy()
            ans+=len(prev)
        return ans
        '''
        
        '''
        queue=[(i,1) for i in range(1,maxValue+1)]
        ans=0
        while queue:
            value,length=queue.pop(0)
            ans+=comb(n-1, length-1)
            if length==n:
                continue
            next=value*2
            while next<=maxValue:
                queue.append((next,length+1))
                next+=value
        return ans%(10**9+7)
        '''

        @lru_cache(None)
        def dfs(value,length):
            res=comb(n-1, length-1)
            next=value*2
            if length==n:
                return res
            while next<=maxValue:
                res+=dfs(next,length+1)
                next+=value
            return res

        ans=sum(dfs(i,1) for i in range(1,maxValue+1))
        return ans%(10**9+7)