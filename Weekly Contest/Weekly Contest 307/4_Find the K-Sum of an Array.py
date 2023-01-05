# 2386. Find the K-Sum of an Array
# https://leetcode.com/problems/find-the-k-sum-of-an-array/

import heapq

class Solution:
    def kSum(self, nums, k):
        '''
        ans=[]

        def rec(idx,path):
            if idx==n:
                ans.append(sum(path))
                return
            rec(idx+1,path)
            rec(idx+1,path+[nums[idx]])

        n=len(nums)
        rec(0,[])
        return heapq.nlargest(ans,k)[-1]
        '''

        maxsum=0
        n=len(nums)
        for i in range(n):
            if nums[i]>=0:
                maxsum+=nums[i]
            else:
                nums[i]=abs(nums[i])
        nums.sort()
        queue=[(nums[0],0)]
        subtract=[]
        while queue and len(subtract)<k-1:
            value,idx=heapq.heappop(queue)
            subtract.append(value)
            if idx+1<n:
                heapq.heappush(queue,(value+nums[idx+1],idx+1))
                heapq.heappush(queue,(value+nums[idx+1]-nums[idx],idx+1))
        ans=[maxsum]
        for i in subtract:
            ans.append(maxsum-i)
        return ans[-1]