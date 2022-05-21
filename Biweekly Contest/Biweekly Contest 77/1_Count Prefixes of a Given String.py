# 2255. Count Prefixes of a Given String
# https://leetcode.com/problems/count-prefixes-of-a-given-string/

class Solution:
    def countPrefixes(self, words, s):
        '''
        return sum(map(s.startswith,words))
        '''
        
        ans=0
        for i in words:
            if s.startswith(i):
                ans+=1
        return ans