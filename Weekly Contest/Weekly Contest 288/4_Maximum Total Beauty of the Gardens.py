# 2234. Maximum Total Beauty of the Gardens
# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/

from bisect import bisect_right

class Solution:
    def maximumBeauty(self, flowers, newFlowers, target, full, partial):
        flowers=[min(target,i) for i in flowers]
        flowers.sort()
        if min(flowers)==target:
            return len(flowers)*full
        if newFlowers>=len(flowers)*target-sum(flowers):
            return max(len(flowers)*full,(len(flowers)-1)*full+partial*(target-1))
        cost=[0]
        for i in range(1,len(flowers)):
            cost.append((flowers[i]-flowers[i-1])*i+cost[-1])
        j=len(flowers)-1
        while flowers[j]==target:
            j-=1
        ans=0
        while newFlowers>=0:
            idx=min(j,bisect_right(cost,newFlowers)-1)
            bar=flowers[idx]+(newFlowers-cost[idx])//(idx+1)
            ans = max(ans, bar * partial + full *(len(flowers) - j - 1))
            newFlowers-=(target-flowers[j])
            j-=1
        return ans