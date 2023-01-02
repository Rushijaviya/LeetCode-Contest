# 2364. Count Number of Bad Pairs
# https://leetcode.com/problems/count-number-of-bad-pairs/

from collections import Counter

class Solution:
    def countBadPairs(self, nums):
        '''
        l=[]
        n=len(nums)
        for i in range(n):
            l.append(nums[i]-i)
        total=0
        count=0
        d={}
        for i in range(n):
            total+=i
            count+=d.get(l[i],0)
            d[l[i]]=d.get(l[i],0)+1
        return total-count
        '''
        
        '''
        nums=[nums[i]-i for i in range(len(nums))]
        c=Counter(nums)
        s=sum(((c[i]-1)*(c[i]))//2 for i in c)
        return (len(nums)*(len(nums)-1))//2 - s
        '''

        n=len(nums)
        count=0
        d={}
        for i in range(n):
            count+=(i-d.get(nums[i]-i,0))
            d[nums[i]-i]=d.get(nums[i]-i,0)+1
        return count