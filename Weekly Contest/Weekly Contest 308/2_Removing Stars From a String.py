# 2390. Removing Stars From a String
# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for i in s:
            if i=='*':
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
        
        '''
        s=list(s)
        idx=0
        for i in s:
            if i=='*':
                idx-=1
            else:
                s[idx]=i
                idx+=1
        return "".join(s[:idx])
        '''