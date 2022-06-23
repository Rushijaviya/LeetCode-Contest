# 2312. Selling Pieces of Wood
# https://leetcode.com/problems/selling-pieces-of-wood/

class Solution:
    def sellingWood(self, m, n, prices):
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i,j,k in prices:
            dp[i][j]=k
        for row in range(1,m+1):
            for col in range(1,n+1):
                for splitcol in range(1,col//2+1):
                    dp[row][col]=max(dp[row][col],dp[row][splitcol]+dp[row][col-splitcol])
                for splitrow in range(1,row//2+1):
                    dp[row][col]=max(dp[row][col],dp[splitrow][col]+dp[row-splitrow][col])
        return dp[m][n]