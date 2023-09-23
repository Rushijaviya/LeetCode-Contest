# 2683. Neighboring Bitwise XOR
# https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution:
    def doesValidArrayExist(self, derived):
        ans=derived[0]
        for num in derived[1:]:
            ans^=num
        return ans==0
    
        # return sum(derived)%2==0