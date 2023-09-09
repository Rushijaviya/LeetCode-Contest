# 2652. Sum Multiples
# https://leetcode.com/problems/sum-multiples/

class Solution:
    def sumOfMultiples(self, n):
        '''
        ans=0
        for num in range(3,n+1):
            if num%3==0 or num%5==0 or num%7==0:
                ans+=num
        return ans
        '''

        x,y,z=n//3,n//5,n//7
        a,b,c=n//15,n//21,n//35
        extra=n//105
        return (3*x*(x+1))//2 + (5*y*(y+1))//2 + (7*z*(z+1))//2 - (15*a*(a+1))//2 - (21*b*(b+1))//2 - (35*c*(c+1))//2 + (105*extra*(extra+1))//2