# 2433. Find The Original Array of Prefix Xor
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

class Solution:
    def findArray(self, pref):
        '''
        ans=[pref[0]]
        for i in range(1,len(pref)):
            ans.append(pref[i]^pref[i-1])
        return ans
        '''

        for i in range(len(pref)-1,0,-1):
            pref[i]^=pref[i-1]
        return pref