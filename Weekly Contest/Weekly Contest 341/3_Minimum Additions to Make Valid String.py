# 2645. Minimum Additions to Make Valid String
# https://leetcode.com/problems/minimum-additions-to-make-valid-string/

class Solution:
    def addMinimum(self, word: str) -> int:
        count,prev=0,'z'
        for char in word:
            count+=(prev>=char)
            prev=char
        return 3*count-len(word)
        
        '''
        idx=0
        ans=0
        while idx<len(word):
            if word[idx:idx+3]=='abc':
                idx+=3
            elif word[idx:idx+2] in ['ab','bc','ac']:
                ans+=1
                idx+=2
            else:
                ans+=2
                idx+=1
        return ans
        '''