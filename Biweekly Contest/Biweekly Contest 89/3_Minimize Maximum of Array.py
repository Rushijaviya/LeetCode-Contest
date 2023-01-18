# 2439. Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/

from math import ceil

class Solution:
    def minimizeArrayValue(self, nums):
        '''
        def vaild(arr,upper_limit):
            for i in range(len(arr)-1,0,-1):
                arr[i-1]+=max(0,arr[i]-upper_limit)
            return arr[0]<=upper_limit

        start=min(nums)
        end=max(nums)
        while start<=end:
            mid=(start+end)//2
            if vaild(nums[:],mid):
                end=mid-1
            else:
                start=mid+1
        return end+1
        '''

        sum=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            sum+=nums[i]
            ans=max(ans,ceil(sum/(i+1)))
        return ans