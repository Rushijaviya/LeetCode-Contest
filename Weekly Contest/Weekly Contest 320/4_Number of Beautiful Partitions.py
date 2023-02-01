# 2478. Number of Beautiful Partitions
# https://leetcode.com/problems/number-of-beautiful-partitions/

from functools import lru_cache

class Solution:
    def beautifulPartitions(self, s, k, minLength):
        '''
        # TLE
        @lru_cache(None)
        def dp(idx,part,prev):
            if idx==n:
                return part==k-1 and idx-prev>=minLength
            ans=dp(idx+1,part,prev)
            if idx-prev+1>=minLength and s[idx] not in prime and (idx+1==n or s[idx+1] in prime):
                ans+=dp(idx+1,part+1,idx+1)
            return ans
            
        prime=['2','3','5','7']
        if s[0] not in prime or s[-1] in prime:
            return 0
        mod=10**9+7
        n=len(s)
        return dp(0,0,0)%mod
        '''
        
        @lru_cache(None)
        def dp(idx,at_start,part):
            if idx==n:
                return part==k
            if idx>n or part==k or (s[idx] not in primes and at_start):
                return 0
            if s[idx] in primes:
                if at_start:
                    return dp(idx+minLength-1,False,part)
                else:
                    return dp(idx+1,False,part)
            return dp(idx+1,True,part+1)+dp(idx+1,False,part)

        n=len(s)
        primes=set('2357')
        mod=10**9+7
        return dp(0,True,0)%mod
        
        '''
        @lru_cache(None)
        def dp(idx,part):
            if part==k-1:
                return ids[idx]+minLength-1<=n-1
            count=0
            for j in range(idx+1,m-(k-part)+2):
                if ids[j]-ids[idx]>=minLength:
                    count+=dp(j,part+1)
            return count

        n=len(s)
        primes=set('2357')
        if s[0] not in primes or s[-1] in primes or k*minLength>n:
            return 0
        ids=[0]
        for i in range(n-1):
            if s[i] not in primes and s[i+1] in primes:
                ids.append(i+1)
        m=len(ids)
        mod=10**9+7
        return dp(0,0)%mod
        '''