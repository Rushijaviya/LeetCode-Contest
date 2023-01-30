# 2472. Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

from functools import lru_cache


class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        '''
        @lru_cache(None)
        def valid(x):
            left=0
            right=len(x)-1
            while left<right and x[left]==x[right]:
                left+=1
                right-=1
            return left>=right

        @lru_cache(None)
        def dp(idx,prev):
            if idx==n:
                return 0
            temp=float('-inf')
            if idx-prev+1>=k and valid(s[prev:idx+1]):
                temp=max(temp,1+dp(idx+1,idx+1))
            else:
                temp=max(temp,dp(idx+1,prev),dp(idx+1,prev+1))
            return temp
        
        n=len(s)
        return dp(0,0)
        '''
        
        def valid(start,end):
            if end>n:
                return 0
            end-=1
            while start<end and s[start]==s[end]:
                start+=1
                end-=1
            return start>=end

        @lru_cache(None)
        def dp(idx):
            if idx==n:
                return 0
            temp=dp(idx+1)
            if valid(idx,idx+k):
                temp=max(temp,1+dp(idx+k))
            if valid(idx,idx+k+1):
                temp=max(temp,1+dp(idx+k+1))
            return temp

        n=len(s)
        return dp(0)
        
        '''
        def valid(start,end):
            end-=1
            while start<end and s[start]==s[end]:
                start+=1
                end-=1
            return start>=end            

        n=len(s)
        dp=[0]*(n+1)
        for i in range(k,n+1):
            dp[i]=dp[i-1]
            if i-k>=0 and valid(i-k,i):
                dp[i]=max(dp[i],1+dp[i-k])
            if i-k-1>=0 and valid(i-k-1,i):
                dp[i]=max(dp[i],1+dp[i-k-1])
        return dp[-1]
        '''