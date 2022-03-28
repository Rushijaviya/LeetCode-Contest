# 2216. Minimum Deletions to Make Array Beautiful
# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/

class Solution:
    def minDeletion(self, nums):
        '''
        # Method 2        
        if not nums:
            return 0
        count=0
        i=0
        while i<len(nums)-1:
            if i%2:
                i+=1    
                continue
            if nums[i]==nums[i+1]:
                nums.pop(i)
                count+=1
            else:
                i+=1
        if len(nums)%2:
            nums.pop()
            count+=1
        return count
        '''

        '''
        # Method 2
        ans=[]
        for i in nums:
            if len(ans)%2==0 or i!=ans[-1]:
                ans.append(i)
        return len(nums)-(len(ans)-len(ans)%2)
        '''

        # Method 3
        ans,prev=0,-1
        for i in nums:
            if i==prev:
                ans+=1
            else:
                if prev<0:
                    prev=i
                else:
                    prev=-1
        return ans if prev<0 else ans+1