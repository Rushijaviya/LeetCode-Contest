# 2643. Row With Maximum Ones
# https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat):
        idx,ans=0,0
        for i in range(len(mat)):
            if mat[i].count(1)>ans:
                ans=mat[i].count(1)
                idx=i
        return [idx,ans]