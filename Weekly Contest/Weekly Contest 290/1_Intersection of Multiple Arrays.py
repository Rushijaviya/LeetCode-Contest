# 2248. Intersection of Multiple Arrays
# https://leetcode.com/problems/intersection-of-multiple-arrays/

class Solution:
    def intersection(self, nums):
        s=set(nums[0])
        for i in nums[1:]:
            s=set(i).intersection(s)
        return sorted(s)

        '''
        d={}
        for i in nums:
            for j in i:
                d[j]=d.get(j,0)+1
        ans=[]
        x=len(nums)
        for i,j in d.items():
            if j==x:
                ans.append(i)
        ans.sort()
        return ans
        '''