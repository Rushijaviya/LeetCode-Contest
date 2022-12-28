# 2351. First Letter to Appear Twice
# https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        '''
        arr=[0]*26
        for i in s:
            if arr[ord(i)-97]:
                return i
            arr[ord(i)-97]=1
        '''
        
        visited=set()
        for i in s:
            if i in visited:
                return i
            visited.add(i)