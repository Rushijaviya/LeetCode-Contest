# 2653. Sliding Subarray Beauty
# https://leetcode.com/problems/sliding-subarray-beauty/

from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums, k, x):
        arr = SortedList(nums[:k])
        ans=[min(arr[x-1],0)]
        for i in range(k,len(nums)):
            arr.remove(nums[i-k])
            arr.add(nums[i])
            ans.append(min(0,arr[x-1]))
        return ans
        
        '''
        arr=[0]*51
        ans=[]
        for i in range(len(nums)):
            if nums[i]<0:
                arr[nums[i]+50]+=1
            if i-k>=0 and nums[i-k]<0:
                arr[nums[i-k]+50]-=1
            if i-k+1<0:
                continue
            count=0
            for i in range(51):
                count+=arr[i]
                if count>=x:
                    ans.append(i-50)
                    break
            else:
                ans.append(0)
        return ans
        '''