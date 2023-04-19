# 2639. Find the Width of Columns of a Grid
# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution:
    def findColumnWidth(self, grid):
        '''
        ans=[]
        for column in zip(*grid):
            temp=0
            for val in column:
                temp=max(temp,len(str(val)) if val>=0 else 1+len(str(abs(val))))
            ans.append(temp)
        return ans
        '''

        return [max(len(str(value)) for value in column) for column in zip(*grid)]