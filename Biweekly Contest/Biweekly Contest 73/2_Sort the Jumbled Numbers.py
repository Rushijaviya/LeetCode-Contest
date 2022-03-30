# 2191. Sort the Jumbled Numbers
# https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping, nums):
        l=[]
        for i in nums:
            s=str(i)
            temp=""
            for j in s:
                temp+=str(mapping[int(j)])
            l.append((int(temp),int(s)))
        l.sort(key=lambda x:x[0])
        ans=[]
        for i,j in l:
            ans.append(j)
        return ans