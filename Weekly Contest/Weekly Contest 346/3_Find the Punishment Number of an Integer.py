# 2698. Find the Punishment Number of an Integer
# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        def valid(num):
            def dp(idx,prev,target):
                if idx==len(s):
                    if idx!=prev:
                        target-=int(s[prev:idx])
                    return target==0
                don=dp(idx+1,prev,target)
                dos=dp(idx+1,idx+1,target-int(s[prev:idx+1]))
                return dos or don

            s=str(num*num)
            return dp(0,0,num)

        ans=0
        for i in range(1,n+1):
            if valid(i):
                ans+=i*i
        return ans
        
        '''
        def valid(num,target):
            if num==target:
                return True
            if num<target or target<0:
                return False
            return valid(num//10,target-num%10) or valid(num//100,target-num%100) or valid(num//1000,target-num%1000)

        ans=0
        for i in range(1,n+1):
            if valid(i*i,i):
                ans+=i*i
        return ans
        '''