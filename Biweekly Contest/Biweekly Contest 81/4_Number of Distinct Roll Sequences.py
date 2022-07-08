# 2318. Number of Distinct Roll Sequences
# https://leetcode.com/problems/number-of-distinct-roll-sequences/

from collections import Counter
from functools import lru_cache

class Solution:
    def distinctSequences(self, n):
        
        '''
        # TLE
        def gcd(a,b):
            if a%b==0:
                return b
            return gcd(b,a%b)
        
        def solve(n,prev,lastprev,i):
            if i==n:
                return 1
            ans=0
            for j in range(1,7):
                if j==prev or j==lastprev or (prev!=-1 and gcd(j,prev)!=1):
                    continue
                ans+=solve(n,j,prev,i+1)
            return ans
        
        return solve(n,-1,-1,0)
        '''

        '''
        # TLE
        def gcd(a,b):
            if a%b==0:
                return b
            return gcd(b,a%b)
        
        def solve(n,prev,lastprev,i):
            if i==n:
                return 1
            if memo[prev][lastprev][i]!=-1:
                return memo[prev][lastprev][i]
            ans=0
            for j in range(1,7):
                if j!=prev and j!=lastprev and (prev==0 or gcd(prev,j)==1):
                    ans+=solve(n,j,prev,i+1)
            memo[prev][lastprev][i]=ans
            return ans
        
        memo=[[[-1]*n for _ in range(7)] for _ in range(7)]
        return solve(n,0,0,0)%(10**9+7)
        '''

        '''
        # TLE
        def gcd(a,b):
            if not a%b:
                return b
            return gcd(b,a%b)
        
        dp=[[[1]*7 for _ in range(7)] for _ in range(n+1)]
        for idx in range(n-1,-1,-1):
            for prev1 in range(7):
                for prev2 in range(7):
                    ans=0
                    for i in range(1,7):
                        if prev1!=i and prev2!=i and (prev1==0 or gcd(prev1,i)==1):
                            ans+=dp[idx+1][i][prev1]
                    dp[idx][prev1][prev2]=ans
        return dp[0][0][0]%(10**9+7)
        '''
        
        '''
        # TLE
        mod = 10**9 + 7
        dp, dp2 = {(7, 7): 1}, Counter()
        for _ in range(n):
            for i, j in dp:
                for k in range(1, 7):
                    if k != i and k != j and gcd(j, k) == 1:
                        dp2[j, k] = (dp2[j, k] + dp[i, j]) % mod
            dp, dp2 = dp2, Counter()
        return sum(dp.values()) % mod
        '''

        m = [[1,2,3,4,5,6], 
         [2,3,4,5,6],
         [1,3,5],
         [1,2,4,5],
         [1,3,5],
         [1,2,3,4,6],
         [1,5]]
        
        @lru_cache(None)
        def dp(prev,lastprev,n):
            if n==0:
                return 1
            ans=0
            for i in m[prev]:
                if i!=lastprev:
                    ans+=dp(i,prev,n-1)
            return ans%(10**9+7)
        
        return dp(0,0,n)


'''
dp = lru_cache()(lambda n,p=0,pp=0:sum(dp(n-1,x,p) for x in range(1,7) if x!=p and x!=pp and (p==0 or gcd(x,p)==1)) % 1000000007 if n else 1)
class Solution: 
    distinctSequences = lambda self, n: dp(n)
'''