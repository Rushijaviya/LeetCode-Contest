# 2522. Partition String Into Substrings With Values at Most K
# https://leetcode.com/problems/partition-string-into-substrings-with-values-at-most-k/

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count=0
        prev=""
        for i in s:
            if int(i)>k:
                return -1
            if int(prev+i)>k:
                count+=1
                prev=i
            else:
                prev+=i
        return count+1