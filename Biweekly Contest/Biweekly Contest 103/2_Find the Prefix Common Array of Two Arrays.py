# 2657. Find the Prefix Common Array of Two Arrays
# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A, B):
        s=set()
        ans=[]
        for i in range(len(A)):
            s.add(A[i])
            s.add(B[i])
            ans.append(2*i+2-len(s))
        return ans