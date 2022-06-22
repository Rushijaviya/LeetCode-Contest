# 2311. Longest Binary Subsequence Less Than or Equal to K
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

class Solution:
    def longestSubsequence(self, s, k):
        
        def solve(i,power,score,dp):
            if i<0:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dos=0
            if s[i]=='1':
                if score+pow(2,power)<=k:
                    dos=1+solve(i-1,power+1,score+pow(2,power),dp)
            else:
                dos=1+solve(i-1,power+1,score,dp)
            don=solve(i-1,power,score,dp)
            dp[i]=max(dos,don)
            return dp[i]
        
        n=len(s)
        power,score=0,0
        dp=[-1]*(n+1)
        return solve(n-1,power,score,dp)

        '''
        idx=len(s)-1
        value=0
        power=1
        count=0
        while idx>=0 and value+power<=k:
            if s[idx]=='1':
                count+=1
                value+=power
            power<<=1
            idx-=1
        return s.count('0')+count
        '''