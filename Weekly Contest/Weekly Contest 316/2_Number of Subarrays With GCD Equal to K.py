# 2447. Number of Subarrays With GCD Equal to K
# https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

from math import gcd

class Solution:
    def subarrayGCD(self, nums, k):
        '''
        ans=0
        n=len(nums)
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr=gcd(curr,nums[j])
                if curr==k:
                    ans+=1
        return ans
        '''
        
        '''
        ans=0
        n=len(nums)
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr=gcd(curr,nums[j])
                if curr==k:
                    ans+=1
                elif curr%k!=0:
                    break
        return ans
        '''

        ans=0
        d={}
        for i in range(len(nums)):
            next={}
            if nums[i]%k==0:
                next[nums[i]]=1
                for j in d:
                    curr=gcd(j,nums[i])
                    next[curr]=next.get(curr,0)+d[j]
            ans+=next.get(k,0)
            d=next
        return ans