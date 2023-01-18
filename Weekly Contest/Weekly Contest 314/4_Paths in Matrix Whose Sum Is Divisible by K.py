# 2435. Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

class Solution:
    def numberOfPaths(self, grid, k):
        '''
        # TLE
        def dp(i,j,s):
            if  (i,j,s) in memo:
                return memo[(i,j,s)]
            if i==m-1 and j==n-1:
                memo[(i,j,s)]=0
                if (s+grid[i][j])%k==0:
                    memo[(i,j,s)]=1
                return memo[(i,j,s)]
            memo[(i,j,s)]=0
            if i<m and j<n:
                memo[(i,j,s)]=dp(i+1,j,(s+grid[i][j])%k)+dp(i,j+1,(s+grid[i][j])%k)
            return memo[(i,j,s)]

        m,n=len(grid),len(grid[0])
        memo={}
        return dp(0,0,0)%(10**9+7)
        '''

        m,n=len(grid),len(grid[0])
        dp=[[[0]*k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]%k]=1
        mod=10**9+7
        for i in range(m):
            for j in range(n):
                for s in range(k):
                    modded_sum = (s + grid[i][j]) % k
                    if i>0:
                        dp[i][j][modded_sum]+=dp[i-1][j][s]
                    if j>0:
                        dp[i][j][modded_sum]+=dp[i][j-1][s]
                    dp[i][j][modded_sum]%=mod
        return dp[-1][-1][0]