# 2565. Subsequence With the Minimum Score
# https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        m,n=len(s),len(t)
        dp=[-1]*n
        idx=n-1
        for i in range(m-1,-1,-1):
            if idx>0 and s[i]==t[idx]:
                dp[idx]=i
                idx-=1
        ans=idx+1
        j=0
        for i in range(m):
            if j<n and s[i]==t[j]:
                while idx<n and dp[idx]<=i:
                    idx+=1
                j+=1
                ans=min(ans,idx-j)
        return max(0,ans)