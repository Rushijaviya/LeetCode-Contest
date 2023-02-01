# 2484. Count Palindromic Subsequences
# https://leetcode.com/problems/count-palindromic-subsequences/

from functools import lru_cache

class Solution:
    def countPalindromes(self, s):
        '''
        # TLE
        @lru_cache(None)
        def dp(idx,prev):
            if len(prev)==5:
                return prev[0]==prev[4] and prev[1]==prev[3]
            if idx==n:
                return 0
            return dp(idx+1,prev+s[idx])%mod+dp(idx+1,prev)%mod
            
        n=len(s)
        mod=10**9+7
        return dp(0,"")
        '''
        
        '''
        # TLE
        @lru_cache(None)
        def dp(idx,prev):
            if idx==n:
                return 0
            count=dp(idx+1,prev)%mod
            if len(prev)<3:
                count+=dp(idx+1,prev+s[idx])
            elif len(prev)==3:
                if s[idx]==prev[1]:
                    count+=dp(idx+1,prev+s[idx])
            elif len(prev)==4:
                if s[idx]==prev[0]:
                    count+=1
            return count%mod
            
        n=len(s)
        mod=10**9+7
        return dp(0,"")
        '''
        
        '''
        @lru_cache(None)
        def dp(idx,first,second,length):
            if idx==n:
                return 0
            count=dp(idx+1,first,second,length)%mod
            if length==0:
                count+=dp(idx+1,s[idx],second,length+1)
            elif length==1:
                count+=dp(idx+1,first,s[idx],length+1)
            elif length==2:
                count+=dp(idx+1,first,second,length+1)
            elif length==3:
                if s[idx]==second:
                    count+=dp(idx+1,first,second,length+1)
            elif length==4:
                if s[idx]==first:
                    count+=1
            return count%mod
            
        n=len(s)
        mod=10**9+7
        ans=dp(0,-1,-1,0)
        dp.cache_clear()
        return ans
        '''
        
        n=len(s)
        count=[0]*10
        pref=[ [[0]*10 for _ in range(10)] for _ in range(n)]
        count[int(s[0])]+=1
        for i in range(1,n):
            char=int(s[i])
            for j in range(10):
                for k in range(10):
                    pref[i][j][k]=pref[i-1][j][k]
                    if char==k:
                        pref[i][j][k]+=count[j]
            count[char]+=1
        count=[0]*10
        suff=[[[0] * 10 for _ in range(10)] for _ in range(n)]
        count[int(s[-1])]+=1
        for i in range(n-2,-1,-1):
            char=int(s[i])
            for j in range(10):
                for k in range(10):
                    suff[i][j][k]=suff[i+1][j][k]
                    if char==k:
                        suff[i][j][k]+=count[j]
            count[char]+=1
        ans=0
        for i in range(2,n-2):
            for j in range(10):
                for k in range(10):
                    ans+=(pref[i-1][j][k]*suff[i+1][j][k])
        return ans%(10**9+7)
        
        '''
        n=len(s)
        mod=10**9+7
        ans=0
        for i in range(10):
            for j in range(10):
                pattern=f"{i}{j}|{j}{i}"
                dp=[0]*6
                dp[-1]=1
                for x in range(n):
                    for y in range(5):
                        if s[x]==pattern[y] or y==2:
                            dp[y]+=dp[y+1]
                ans+=dp[0]
        return ans%mod
        '''