# 2430. Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/

class Solution:
    def deleteString(self, s: str) -> int:
        if len(set(s))==1:
            return len(s)
        n=len(s)
        lcs=[[0]*(n+1) for _ in range(n+1)]
        dp=[1]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    lcs[i][j]=lcs[i+1][j+1]+1
                if lcs[i][j]>=(j-i):
                    dp[i]=max(dp[i],dp[j]+1)
        return dp[0]
        
        '''
        if len(set(s))==1:
            return len(s)
        
        @lru_cache(None)
        def rec(idx):
            if idx==n:
                return 0
            ans=1
            j=1
            while idx+2*j<=n and n-idx-j+1>ans:
                if s[idx:idx+j]==s[idx+j:idx+2*j]:
                    ans=max(ans,1+rec(idx+j))
            return ans

        n=len(s)
        return rec(0)
        '''