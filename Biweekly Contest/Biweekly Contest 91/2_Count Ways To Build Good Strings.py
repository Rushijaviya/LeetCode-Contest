# 2466. Count Ways To Build Good Strings
# https://leetcode.com/problems/count-ways-to-build-good-strings/

from collections import Counter

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        '''
        # TLE
        @lru_cache(None)
        def dp(s):
            if len(s)>high:
                return 0
            if low<=len(s):
                temp=1+dp(s+'0'*zero)+dp(s+'1'*one)
            else:
                temp=dp(s+'0'*zero)+dp(s+'1'*one)
            return temp
        return dp("")
        '''
        
        '''
        @lru_cache(None)
        def dfs(i):
            if i<=0:
                return i==0
            return (dfs(i-one)+dfs(i-zero))%(10**9+7)
        
        dfs(high)
        return sum(dfs(i) for i in range(low,high+1))%(10**9+7)
        '''

        dp=Counter({0:1})
        for i in range(1,high+1):
            dp[i]=dp[i-one]+dp[i-zero]
        return sum(dp[i] for i in range(low,high+1))%(10**9+7)