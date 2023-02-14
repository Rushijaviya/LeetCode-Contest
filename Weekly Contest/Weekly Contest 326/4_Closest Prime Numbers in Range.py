# 2523. Closest Prime Numbers in Range
# https://leetcode.com/problems/closest-prime-numbers-in-range/

from math import sqrt

class Solution:
    def closestPrimes(self, left: int, right: int):

        def isprime(num):
            if num==1:
                return False
            for i in range(2,int(sqrt(num))+1):
                if num%i==0:
                    return False
            return True

        ans=[-1,-1]
        prev=-1
        for num in range(left,right+1):
            if isprime(num):
                if ans[0]==-1:
                    ans[0]=num
                elif ans[1]==-1:
                    ans[1]=num
                    prev=num
                    if ans[1]-ans[0]<3:
                        return ans
                elif ans[1]-ans[0]>num-prev:
                    ans=[prev,num]
                    if ans[1]-ans[0]<3:
                        return ans
                prev=num
        return ans if ans[1]!=-1 else [-1,-1]

        '''
        primes=[True]*(right+1)
        primes[0]=primes[1]=False
        for i in range(2,right+1):
            if primes[i]:
                for j in range(i*i,right+1,i):
                    primes[j]=False
        
        
        possible=[i for i in range(left,right+1) if primes[i]]
        if len(possible)<2:
            return [-1,-1]
        ans=[possible[0],possible[1]]
        for i,j in zip(possible[1:],possible[2:]):
            if ans[1]-ans[0]>j-i:
                ans=[i,j]
                if ans[1]-ans[0]<3:
                    return ans
        return ans
        '''