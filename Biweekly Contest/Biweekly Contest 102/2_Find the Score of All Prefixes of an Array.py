# 2640. Find the Score of All Prefixes of an Array
# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/

class Solution:
    def findPrefixScore(self, nums):
        '''
        conversion=[]
        max_value=float('-inf')
        for num in nums:
            max_value=max(max_value,num)
            conversion.append(num+max_value)
        return list(accumulate(conversion))
        '''

        conversion=[0]
        max_value=float('-inf')
        for num in nums:
            max_value=max(max_value,num)
            conversion.append(max_value+num+conversion[-1])
        return conversion[1:]