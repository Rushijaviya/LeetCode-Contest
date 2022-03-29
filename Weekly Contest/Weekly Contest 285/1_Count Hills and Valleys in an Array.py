# 2210. Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums):
        count=0
        l=[nums[0]]
        for i in nums:
            if i!=l[-1]:
                l.append(i)
        for i in range(1,len(l)-1):
            if (l[i]>l[i-1] and l[i]>l[i+1]) or (l[i]<l[i-1] and l[i]<l[i+1]):
                count+=1
        return count

        '''
        count=0
        left=nums[0]
        for i in range(1,len(nums)-1):
            if (nums[i]>left and nums[i]>nums[i+1]) or (nums[i]<left and nums[i]<nums[i+1]):
                count+=1
                left=nums[i]
        return count
        '''        