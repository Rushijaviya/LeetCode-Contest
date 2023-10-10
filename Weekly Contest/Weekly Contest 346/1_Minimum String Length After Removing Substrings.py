# 2696. Minimum String Length After Removing Substrings
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/

class Solution:
    def minLength(self, s: str) -> int:
        '''
        while 'AB' in s or 'CD' in s:
            if 'AB' in s:
                idx=s.index('AB')
                s=s[:idx]+s[idx+2:]
            if 'CD' in s:
                idx=s.index('CD')
                s=s[:idx]+s[idx+2:]
        return len(s)
        '''

        stack=[]
        for char in s:
            if stack and (stack[-1]+char=='AB' or stack[-1]+char=='CD'):
                stack.pop()
            else:
                stack.append(char)
        return len(stack)