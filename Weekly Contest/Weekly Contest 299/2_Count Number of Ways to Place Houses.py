# 2320. Count Number of Ways to Place Houses
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

class Solution:
    def countHousePlacements(self, n):
        '''
        @lru_cache(None)
        def dp(idx,last):
            if idx==n:
                return 1
            if last:
                return dp(idx+1,0)
            return dp(idx+1,1)+dp(idx+1,0)

        x=dp(0,0)
        return (x*x)%(10**9+7)
        '''
        
        '''
        x,y=0,1
        for i in range(n):
            x,y=y,x+y
        return (y*y)%(10**9+7)
        '''

        # fibonacci
        x,y=1,2
        for i in range(1,n):
            x,y=y,x+y
        return (y*y)%(10**9+7)