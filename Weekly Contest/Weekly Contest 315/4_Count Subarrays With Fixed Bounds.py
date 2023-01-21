# 2444. Count Subarrays With Fixed Bounds
# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums, minK, maxK):
        '''
        def rec(idx,temp):
            ans.add(tuple(temp))
            if idx==len(nums):
                return
            rec(idx+1,temp+[idx])
            rec(idx+1,[idx])
            
            
        ans=set()
        rec(0,[])
        count=0
        ans.remove(tuple([]))
        for i in ans:
            i=set(map(lambda x:nums[x],i))
            if min(i)==minK and max(i)==maxK:
                count+=1
        return count
        '''

        '''
        n=len(nums)
        count=0
        for i in range(n):
            left,right=nums[i],nums[i]
            for j in range(i,n):
                left=min(left,nums[j])
                right=max(right,nums[j])
                if left==minK and right==maxK:
                    count+=1
        return count
        '''

        ans=0
        prevmin=prevmax=previnvaild=-1
        for i in range(len(nums)):
            if nums[i]==minK:
                prevmin=i
            if nums[i]==maxK:
                prevmax=i
            if not minK<=nums[i]<=maxK:
                previnvaild=i
            ans+=max(0,min(prevmax,prevmin)-previnvaild)
        return ans