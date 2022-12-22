# 2327. Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        '''
        dp=[0]*1001
        dp[1]=1
        for i in range(1,n+1):
            if dp[i]>0:
                for j in range(i+delay,min(i+forget,1001)):
                    dp[j]+=dp[i]
        ans=0
        for i in range(1,n+1):
            if i+forget>n:
                ans+=dp[i]
        return ans%(10**9+7)
        '''
        
        dp=[0]*1002
        dp[1]=1
        dp[2]=-1 # handle the case when delay>1
        ans=0
        curr=0
        for i in range(1,n+1):
            curr+=dp[i]
            if i+forget>n:
                ans+=curr
            if curr>0:
                dp[min(i+delay,1001)]+=curr
                dp[min(i+forget,1001)]-=curr
        return ans%(10**9+7)
        
        '''
        def dp(i):
            if not i:
                return 0
            if i in memo:
                return memo[i]
            ans=1
            for j in range(delay,forget):
                if i-j>0:
                    ans+=dp(i-j)
            memo[i]=ans
            return memo[i]

        memo={}
        return (dp(n)-dp(n-forget))%(10**9+7)
        '''