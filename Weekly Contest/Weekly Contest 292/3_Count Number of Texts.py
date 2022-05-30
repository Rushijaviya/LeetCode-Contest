# 2266. Count Number of Texts
# https://leetcode.com/problems/count-number-of-texts/

class Solution:
    def countTexts(self, pressedKeys):
        n=len(pressedKeys)
        dp=[0]*(n+1)
        MOD=10**9+7
        dp[0]=1
        for i in range(1,n+1):
            dp[i]=dp[i-1]
            if i-2>=0 and pressedKeys[i-1]==pressedKeys[i-2]:
                dp[i]+=dp[i-2]
                if i-3>=0 and pressedKeys[i-1]==pressedKeys[i-3]:
                    dp[i]+=dp[i-3]
                    if pressedKeys[i-1] in "79" and i-4>=0 and pressedKeys[i-1]==pressedKeys[i-4]:
                        dp[i]+=dp[i-4]
                dp[i]%=MOD
        return dp[-1]%MOD
        
        '''
        n=len(pressedKeys)
        dp=[0]*5
        MOD=10**9+7
        dp[0]=1
        for i in range(1,n+1):
            dp[i%5]=dp[(i-1)%5]
            if i-2>=0 and pressedKeys[i-1]==pressedKeys[i-2]:
                dp[i%5]+=dp[(i-2)%5]
                if i-3>=0 and pressedKeys[i-1]==pressedKeys[i-3]:
                    dp[i%5]+=dp[(i-3)%5]
                    if pressedKeys[i-1] in "79" and i-4>=0 and pressedKeys[i-1]==pressedKeys[i-4]:
                        dp[i%5]+=dp[(i-4)%5]
            dp[i%5]%=MOD
        return dp[n%5]%MOD
        '''

        '''
        keys = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        @lru_cache(None)
        def dfs(k):
            if k == len(pressedKeys): return 1
            prev = pressedKeys[k]
            count = 0
            for x in keys[int(pressedKeys[k])]:
                k += 1
                count += dfs(k)
                if(k == len(pressedKeys) or pressedKeys[k] != prev) : break;
            return count % int(1e9 + 7)
        return dfs(0)
        '''