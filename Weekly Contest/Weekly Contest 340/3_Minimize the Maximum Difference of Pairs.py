# 2616. Minimize the Maximum Difference of Pairs
# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution:
    def minimizeMax(self, nums, p):

        def valid(target):
            count=0
            idx=1
            while idx<len(nums):
                if nums[idx]-nums[idx-1]<=target:
                    idx+=1
                    count+=1
                idx+=1
            return count>=p

        nums.sort()
        start=0
        end=nums[-1]-nums[0]
        while start<=end:
            mid=(start+end)//2
            if valid(mid):
                end=mid-1
            else:
                start=mid+1
        return end+1