# 2496. Maximum Value of a String in an Array
# https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution:
    def maximumValue(self, strs):
        '''
        return max(map(lambda x:int(x) if x.isnumeric() else len(x),strs))
        '''

        ans=0
        for i in strs:
            try:
                ans=max(ans,int(i))
            except:
                ans=max(ans,len(i))
        return ans