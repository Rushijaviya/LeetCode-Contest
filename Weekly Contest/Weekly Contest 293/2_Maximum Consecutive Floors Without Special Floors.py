# 2274. Maximum Consecutive Floors Without Special Floors
# https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

class Solution:
    def maxConsecutive(self, bottom, top, special):
        special.sort()
        n=len(special)
        ans=special[0]-bottom
        for i in range(1,n):
            ans=max(ans,special[i]-special[i-1]-1)
        return max(ans,top-special[-1])