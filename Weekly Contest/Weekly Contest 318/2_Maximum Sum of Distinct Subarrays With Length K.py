# 2461. Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums, k):
        '''
        sum=0
        left=0
        visited=set()
        length=0
        n=len(nums)
        ans=0
        for right in range(n):
            while length==k or nums[right] in visited:
                visited.remove(nums[left])
                sum-=nums[left]
                length-=1
                left+=1
            visited.add(nums[right])
            sum+=nums[right]
            length+=1
            if length==k:
                ans=max(ans,sum)
        return ans
        '''
        
        d={}
        sum=0
        for i in range(k):
            d[nums[i]]=d.get(nums[i],0)+1
            sum+=nums[i]
        ans=sum if len(d)==k else 0
        for i in range(k,len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
            sum+=nums[i]
            d[nums[i-k]]-=1
            sum-=nums[i-k]
            if d[nums[i-k]]==0:
                del d[nums[i-k]]
            if len(d)==k:
                ans=max(ans,sum)
        return ans
        
        '''
        arr=[-1]*100001
        sum=0
        ans=0
        dup=-1
        for i in range(len(nums)):
            sum+=nums[i]
            if i>=k:
                sum-=nums[i-k]
            dup=max(dup,arr[nums[i]])
            if i-dup>=k:
                ans=max(ans,sum)
            arr[nums[i]]=i
        return ans
        '''