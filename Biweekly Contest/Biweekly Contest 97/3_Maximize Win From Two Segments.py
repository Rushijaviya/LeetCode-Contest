# 2555. Maximize Win From Two Segments
# https://leetcode.com/problems/maximize-win-from-two-segments/

class Solution:
    def maximizeWin(self, prizePositions, k):
        left=0
        n=len(prizePositions)
        ans=0
        dp=[0]*n
        for right in range(n):
            while prizePositions[right]-prizePositions[left]>k:
                left+=1
            ans=max(ans,right-left+1+(dp[left-1] if left>0 else 0))
            dp[right]=max(dp[right-1] if right>0 else 0,right-left+1)
        return ans