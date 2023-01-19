# 2443. Sum of Number and Its Reverse
# https://leetcode.com/problems/sum-of-number-and-its-reverse/

class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        '''
        if num==0:
            return True
        for i in range(num):
            if i+int(str(i)[::-1])==num:
                return True
        return False
        '''

        def reverse(x):
            ans=0
            while x>0:
                ans=ans*10+x%10
                x//=10
            return ans

        for i in range(num//2,num+1):
            if i+reverse(i)==num:
                return True
        return False