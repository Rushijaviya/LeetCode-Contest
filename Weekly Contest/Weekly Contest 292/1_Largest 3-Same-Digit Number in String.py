# 2264. Largest 3-Same-Digit Number in String
# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution:
    def largestGoodInteger(self, num):
        for i in range(9,-1,-1):
            if (str(i)*3) in num:
                return str(i)*3
        return ""
        
        '''
        ans=""
        n=len(num)
        for i in range(1,n-1):
            if num[i]==num[i-1] and num[i]==num[i+1]:
                ans=max(ans,num[i-1:i+2])
        return ans
        '''
        
        '''
        return max(num[i-2:i+1] if num[i]==num[i-1] and num[i]==num[i-2] else "" for i in range(2,len(num)))
        '''