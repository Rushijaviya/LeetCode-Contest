# 2309. Greatest English Letter in Upper and Lower Case
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

from collections import Counter

class Solution:
    def greatestLetter(self, s):
        c=Counter(s)
        for i in range(25,-1,-1):
            if chr(i+65) in c and chr(i+97) in c:
                return chr(i+65)
        return ""
        
        '''
        upper,lower=[0]*26,[0]*26
        for i in s:
            if ord(i) in range(97,123):
                lower[ord(i)-97]=1
            else:
                upper[ord(i)-65]=1
        for i in range(25,-1,-1):
            if upper[i] and lower[i]:
                return chr(i+65)
        return ""
        '''