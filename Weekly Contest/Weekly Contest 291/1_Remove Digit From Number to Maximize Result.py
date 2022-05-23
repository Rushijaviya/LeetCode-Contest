# 2259. Remove Digit From Number to Maximize Result
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number, digit):
        '''
        ans=[]
        l=list(number)
        n=len(l)
        for i in range(n):
            if l[i]==digit:
                ans.append(l[:i]+l[i+1:])
        return "".join(max(ans))
        '''

        n=len(number)
        for i in range(n-1):
            if number[i]==digit and number[i+1]>digit:
                return number[:i]+number[i+1:]
        d=number[::-1].index(digit)
        d=n-d-1
        return number[:d]+number[d+1:]