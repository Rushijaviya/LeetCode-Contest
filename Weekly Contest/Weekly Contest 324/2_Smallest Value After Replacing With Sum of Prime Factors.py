# 2507. Smallest Value After Replacing With Sum of Prime Factors
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

from math import sqrt

class Solution:
    def smallestValue(self, n: int) -> int:
        '''
        if n==4:
            return 4
        def isprime(x):
            for i in range(2,int(sqrt(x))+1):
                if x%i==0:
                    return False
            return True
        
        while True:
            sum=0
            for i in range(2,n):
                while n%i==0 and isprime(i):
                    sum+=i
                    n//=i
            if sum==0:
                return n
            n=sum
        '''
        
        if n==4:
            return 4
        while True:
            sum=0
            for i in range(2,n):
                while n%i==0:
                    sum+=i
                    n//=i
            if sum==0:
                return n
            n=sum
        
        '''
        def rec(num):
            if num==4:
                return num
            sum=0
            for i in range(2,num):
                while num%i==0:
                    sum+=i
                    num//=i
            if sum==0:
                return num
            return rec(sum)

        return rec(n)
        '''