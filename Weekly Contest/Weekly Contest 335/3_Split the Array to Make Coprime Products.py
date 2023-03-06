# 2584. Split the Array to Make Coprime Products
# https://leetcode.com/problems/split-the-array-to-make-coprime-products/

from collections import Counter
from math import sqrt

class Solution:
    def findValidSplit(self, nums):
        '''
        # TLE
        pref=nums[0]
        suf=reduce(lambda x,y:x*y,nums[1:])
        if gcd(pref,suf)==1:
            return 0
        for i in range(1,len(nums)-1):
            pref*=nums[i]
            suf//=nums[i]
            if gcd(pref,suf)==1:
                return i
        return -1
        '''
        
        freq=Counter()
        for num in nums:
            for x in range(2,int(sqrt(num))+1):
                while num%x==0:
                    freq[x]+=1
                    num//=x
            if num>1:
                freq[num]+=1
        prefix=Counter()
        overlap=0
        for idx in range(len(nums)-1):
            for x in range(2,int(sqrt(nums[idx]))+1):
                if nums[idx]%x==0:
                    if prefix[x]==0:
                        overlap+=1
                    while nums[idx]%x==0:
                        nums[idx]//=x
                        prefix[x]+=1
                    if prefix[x]==freq[x]:
                        overlap-=1
            if nums[idx]>1:
                if prefix[nums[idx]]==0:
                    overlap+=1
                prefix[nums[idx]]+=1
                if prefix[nums[idx]]==freq[nums[idx]]:
                    overlap-=1
            if overlap==0:
                return idx
        return -1
        
        '''
        last_seen_idx={}
        for idx,num in enumerate(nums):
            for x in range(2,int(sqrt(num))+1):
                if num%x==0:
                    last_seen_idx[x]=idx
                    while num%x==0:
                        num//=x
            if num:
                last_seen_idx[num]=idx
        right_most_idx=0
        for idx,num in enumerate(nums):
            if idx==len(nums)-1:
                continue
            for x in range(2,int(sqrt(num))+1):
                if num%x==0:
                    right_most_idx=max(right_most_idx,last_seen_idx[x])
                    while num%x==0:
                        num//=x
            if num:
                right_most_idx=max(right_most_idx,last_seen_idx[num])
            if right_most_idx==idx:
                return idx
        return -1
        '''