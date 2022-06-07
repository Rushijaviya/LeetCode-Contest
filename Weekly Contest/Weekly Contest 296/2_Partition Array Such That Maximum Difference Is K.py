# 2294. Partition Array Such That Maximum Difference Is K
# https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

class Solution:
    def partitionArray(self, nums, k):
        '''
        nums.sort()
        stack=[nums[0]]
        for i in nums[1:]:
            if i-stack[-1]>k:
                stack.append(i)
        return len(stack)
        '''

        '''
        nums.sort()
        mn,mx=nums[0],nums[0]
        ans=1
        for i in nums[1:]:
            mn=min(mn,i)
            mx=max(mx,i)
            if mx-mn>k:
                mx=mn=i
                ans+=1
        return ans
        '''
        
        nums.sort()
        ans=1
        prev=nums[0]
        for i in nums[1:]:
            if i-prev>k:
                ans+=1
                prev=i
        return ans