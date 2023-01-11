# 2420. Find All Good Indices
# https://leetcode.com/problems/find-all-good-indices/

class Solution:
    def goodIndices(self, nums, k):
        '''
        n=len(nums)
        ans=[]
        for i in range(k,n-k):
            for j in range(i-k+1,i):
                if nums[j]>nums[j-1]:
                    break
            else:
                for j in range(i+1,i+k):
                    if nums[j]>nums[j+1]:
                        break
                else:
                    ans.append(i)
        return ans
        '''
        
        '''
        n=len(nums)
        before=[]
        for i in range(0,min(k,n)):
            while before and nums[i]>nums[before[-1]]:
                before.pop()
            before.append(i)
        after=[]
        for i in range(k+1,min(n,k+k+1)):
            while after and nums[i]<nums[after[-1]]:
                after.pop()
            after.append(i)
        ans=[]
        for i in range(k,n-k):
            if len(after)==k and len(before)==k:
                ans.append(i)
            if i+k+1==n:
                break
            if before and i-before[0]==k:
                before.pop(0)
            if after and after[0]==i+1:
                after.pop(0)
            while before and nums[i]>nums[before[-1]]:
                before.pop()
            before.append(i)
            while after and nums[i+k+1]<nums[after[-1]]:
                after.pop()
            after.append(i+k+1)
        return ans
        '''

        n=len(nums)
        last=[1]*n
        next=[1]*n
        for i in range(1,n):
            if nums[i]<=nums[i-1]:
                last[i]+=last[i-1]
        for i in range(n-2,-1,-1):
            if nums[i]<=nums[i+1]:
                next[i]+=next[i+1]
        ans=[]
        for i in range(k,n-k):
            if last[i-1]>=k and next[i+1]>=k:
                ans.append(i)
        return ans