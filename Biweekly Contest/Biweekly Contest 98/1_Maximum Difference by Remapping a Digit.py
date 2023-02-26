# 2566. Maximum Difference by Remapping a Digit
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num):
        '''
        max_val=str(num)
        for char in max_val:
            if char!='9':
                max_val=max_val.replace(char,'9')
                break
        min_val=str(num)
        min_val=min_val.replace(min_val[0],'0')
        return int(max_val)-int(min_val)
        '''

        s=str(num)
        for i in range(len(s)):
            if s[i]!='9':
                break
        max_val=s.replace(s[i],'9')
        min_val=s.replace(s[0],'0')
        return int(max_val)-int(min_val)