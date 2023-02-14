# 2521. Distinct Prime Factors of Product of Array
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

from functools import reduce
from math import sqrt

class Solution:
    def distinctPrimeFactors(self, nums):
        '''
        def isprime(num):
            for x in range(2,int(sqrt(num))+1):
                if num%x==0:
                    return False
            return True

        temp=reduce(lambda x,y:x*y,nums)
        count=0
        for i in range(2,1000):
            if temp%i==0 and isprime(i):
                count+=1
        return count
        '''
        
        '''
        def isprime(num):
            for x in range(2,int(sqrt(num))+1):
                if num%x==0:
                    return False
            return True

        nums=set(nums)
        ans=set()
        for num in nums:
            start=2
            while num!=1:
                while num%start==0:
                    num//=start
                    if isprime(start):
                        ans.add(start)
                start+=1
        return len(ans)
        '''

        prime=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        nums=set(nums)
        s=set()
        for num in nums:
            for p in prime:
                if num%p==0:
                    s.add(p)
                    while num%p==0:
                        num//=p
            if num>1:
                s.add(num)
        return len(s)
