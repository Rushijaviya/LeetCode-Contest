# 2194. Cells in a Range on an Excel Sheet
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s):
        start_row,end_row=int(s[1]),int(s[4])
        start_col,end_col=ord(s[0]),ord(s[3])
        ans=[]
        for i in range(start_col,end_col+1):
            for j in range(start_row,end_row+1):
                ans.append(chr(i)+str(j))
        return ans