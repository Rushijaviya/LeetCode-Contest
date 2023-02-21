# 2546. Apply Bitwise Operations to Make Strings Equal
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        # return int(s,2)+int(target,2)==0 or (int(s,2)!=0 and int(target,2)!=0)
        
        return max(s)==max(target)