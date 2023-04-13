# 2610. Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

from collections import Counter

class Solution:
    def findMatrix(self, nums):
        c=Counter(nums)
        ans=[]
        while c:
            path=[]
            next={}
            for value in c:
                path.append(value)
                if c[value]>1:
                    next[value]=c[value]-1
            ans.append(path)
            c=next
        return ans