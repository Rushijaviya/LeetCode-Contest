# 2239. Find Closest Number to Zero
# https://leetcode.com/problems/find-closest-number-to-zero/

class Solution:
    def findClosestNumber(self, nums):
        x=min(nums,key=lambda x:abs(x))
        return x if x>0 or -x not in nums else -x
        
        '''        
        return max([-abs(i),i] for i in nums)[1]
        '''

        '''
        nums.sort(key=lambda x:abs(x))
        x=nums[0]
        idx=1
        ans=x
        while idx<len(nums) and abs(nums[idx])==abs(x):
            ans=max(ans,nums[idx])
            idx+=1
        return ans
        '''