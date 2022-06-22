# 2310. Sum of Numbers With Units Digit K
# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

class Solution:
    def minimumNumbers(self, num, k):
        if not num: return 0
        for i in range(1,11):
            if num%10 == k*i %10 and num>=i*k:
                return i
        return -1

        '''        
        def getnum(digit,k):
            for times in range(1,11):
                if digit==(k*times)%10:
                    return times
            return -1
        
        if num==0:
            return 0
        
        unit_digit=num%10
        ans=getnum(unit_digit,k)
        return ans if num>=ans*k and ans!=-1 else -1
        '''

        '''
        def coinchange(coins,amount):
            dp=[float('inf')]*(amount+1)
            dp[0]=0
            for i in range(amount+1):
                for j in range(len(coins)):
                    if coins[j]<=i and dp[i-coins[j]]!=float('inf'):
                        dp[i]=min(dp[i],dp[i-coins[j]]+1)
            return dp[amount] if dp[amount]!=float('inf') else -1

        coins=[]
        for i in range(num+1):
            if i%10==k:
                coins.append(i)
        return coinchange(coins,num)
        '''