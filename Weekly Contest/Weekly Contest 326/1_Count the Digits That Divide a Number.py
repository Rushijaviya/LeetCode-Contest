# 2520. Count the Digits That Divide a Number
# https://leetcode.com/problems/count-the-digits-that-divide-a-number/

class Solution:
    def countDigits(self, num: int) -> int:
        '''
        count=0
        x=num
        while x:
            count+=(num%(x%10)==0)
            x//=10
        return count
        '''

        return sum(num%int(char)==0 for char in str(num))