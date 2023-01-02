# 2366. Minimum Replacements to Sort the Array
# https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums):
        idx=len(nums)-2
        prev=nums[-1]
        ans=0
        while idx>=0:
            if nums[idx]<=prev:
                prev=nums[idx]
                idx-=1
            else:
                if nums[idx]%prev==0:
                    count=nums[idx]//prev
                else:
                    count=nums[idx]//prev + 1
                    prev=nums[idx]//count
                ans+=(count-1)
                idx-=1
        return ans
        
        '''
        prev=nums[-1]
        ans=0
        for i in range(len(nums)-2,-1,-1):
            count=nums[i]//prev
            if nums[i]%prev:
                count+=1
                prev=nums[i]//count
            ans+=(count-1)
        return ans
        '''