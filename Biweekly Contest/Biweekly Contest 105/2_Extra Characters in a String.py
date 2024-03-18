# 2707. Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/

from functools import lru_cache

class Solution:
    def minExtraChar(self, s, dictionary):
        @lru_cache(None)
        def dp(idx,prev):
            if idx==n:
                return 0 if s[prev:idx] in dictionary else idx-prev
            ans=min(dp(idx+1,prev),1+dp(idx+1,prev+1))
            if s[prev:idx+1] in dictionary:
                ans=min(ans,dp(idx+1,idx+1))
            return ans
        
        n=len(s)
        dictionary=set(dictionary)
        return dp(0,0)
        
        '''
        @lru_cache(None)
        def dp(idx):
            if idx==n:
                return 0
            ans=float('inf')
            for j in range(idx,n):
                if s[idx:j+1] in dictionary:
                    ans=min(ans,dp(j+1))
            ans=min(ans,1+dp(idx+1))
            return ans

        n=len(s)
        dictionary=set(dictionary)
        return dp(0)
        '''