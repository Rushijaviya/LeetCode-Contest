# 2256. Minimum Average Difference
# https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums):
        if len(nums)==1:
            return 0
        n=len(nums)
        front_sum,back_sum=nums[0],sum(nums[1:])
        ans=abs(front_sum-(back_sum//(n-1)))
        index=0
        for i in range(1,n):
            front_sum+=nums[i]
            back_sum-=nums[i]
            a=front_sum//(i+1)
            b=back_sum//(n-1-i) if i!=n-1 else 0
            if ans>abs(a-b):
                ans=abs(a-b)
                index=i
        return index