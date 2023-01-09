# 2400. Number of Ways to Reach a Position After Exactly k Steps
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

from math import comb

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        '''
        def dp(idx,step):
            if step==k:
                return idx==endPos
            if (idx+1,step+1) not in memo:
                memo[(idx+1,step+1)]=dp(idx+1,step+1)
            if (idx-1,step+1) not in memo:
                memo[(idx-1,step+1)]=dp(idx-1,step+1)
            return memo[(idx+1,step+1)]+memo[(idx-1,step+1)]

        memo={}
        return dp(startPos,0)%(10**9+7)
        '''
        
        '''
        @lru_cache(None)        
        def dp(idx,step):
            if step==k:
                return idx==endPos
            if abs(endPos-idx)>(k-step):    # optimization
                return 0
            return dp(idx+1,step+1)+dp(idx-1,step+1)

        return dp(startPos,0)%(10**9+7)
        '''

        if abs(endPos-startPos)>k or  (startPos-endPos-k)%2:
            return 0
        return comb(k,(endPos-startPos+k)//2)%(10**9+7)