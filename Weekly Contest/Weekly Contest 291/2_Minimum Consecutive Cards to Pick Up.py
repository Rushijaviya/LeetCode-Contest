# 2260. Minimum Consecutive Cards to Pick Up
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution:
    def minimumCardPickup(self, cards):
        d={}
        ans=float('inf')
        n=len(cards)
        for i in range(n):
            if cards[i] in d:
                ans=min(ans,i-d[cards[i]]+1)
            d[cards[i]]=i
        return ans if ans!=float('inf') else -1