# 2486. Append Characters to String to Make Subsequence
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        idx=0
        for i in range(len(s)):
            if s[i]==t[idx]:
                idx+=1
                if idx==len(t):
                    break
        return len(t)-idx
        
        '''
        it=iter(s)
        for idx,val in enumerate(t):
            if val not in it:
                return len(t)-idx
        return 0
        '''