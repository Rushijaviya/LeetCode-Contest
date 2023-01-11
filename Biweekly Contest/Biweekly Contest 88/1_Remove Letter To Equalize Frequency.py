# 2423. Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        '''
        c=Counter(word)
        for i in range(26):
            x=chr(i+97)
            if x in c:
                c[x]-=1
                if c[x]==0:
                    del c[x]
                if len(set(c.values()))==1:
                    return True
                c[x]+=1
        return False
        '''
        
        for i in range(len(word)):
            if len(set(Counter(word[:i]+word[i+1:]).values()))==1:
                return True
        return False
        
        '''
        c=Counter(Counter(word).values())
        if len(c)==1:
            return list(c.keys())[0]==1 or list(c.values())[0]==1
        if len(c)==2:
            x,y=min(c.keys()),max(c.keys())
            return (x+1==y and c[y]==1) or (x==1 and c[x]==1)
        return False
        '''