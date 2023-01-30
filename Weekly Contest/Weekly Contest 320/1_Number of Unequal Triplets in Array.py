# 2475. Number of Unequal Triplets in Array
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/

from collections import Counter
from itertools import accumulate

class Solution:
    def unequalTriplets(self, nums):
        '''
        count=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]==nums[i]:
                    continue
                for k in range(j+1,n):
                    if nums[k]!=nums[i] and nums[k]!=nums[j]:
                        count+=1
        return count
        '''
        
        '''
        l=list(Counter(nums).values())
        count=0
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                for k in range(j+1,len(l)):
                    count+=(l[i]*l[j]*l[k])
        return count
        '''
        
        '''
        l=list(accumulate(Counter(nums).values()))
        count=0
        for i in range(1,len(l)-1):
            count+=((l[i-1])*(l[i]-l[i-1])*(l[-1]-l[i]))
        return count
        '''
        
        '''
        c=Counter(nums)
        next=len(nums)
        prev=0
        count=0
        for curr in c:
            next-=c[curr]
            count+=(next*prev*c[curr])
            prev+=c[curr]
        return count
        '''

        total_pairs=0
        ans=0
        c=Counter()
        for idx,value in enumerate(nums):
            pairs_with=c[value]*(idx-c[value])
            pairs_without=total_pairs-pairs_with
            ans+=pairs_without
            total_pairs+=(idx-c[value])
            c[value]+=1
        return ans