# 2261. K Divisible Elements Subarrays
# https://leetcode.com/problems/k-divisible-elements-subarrays/

class Solution:
    def countDistinct(self, nums, k, p):     
        s=set()
        n=len(nums)
        for i in range(n):
            temp=''
            count=0
            for j in range(i,n):
                if nums[j]%p==0:
                    count+=1
                if count>k:
                    break
                temp+=str(nums[j])
                temp+=','
                s.add(temp)
        return len(s)
        
        '''
        trie={}
        n=len(nums)
        ans=0
        for i in range(n):
            count=0
            cur=trie
            for j in range(i,n):
                if nums[j]%p==0:
                    count+=1
                if count>k:
                    break
                if nums[j] not in cur:
                    cur[nums[j]]={}
                    ans+=1
                cur=cur[nums[j]]
        return ans
        '''