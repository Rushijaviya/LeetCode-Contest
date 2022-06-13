# 2301. Match Substring After Replacement
# https://leetcode.com/problems/match-substring-after-replacement/

from collections import defaultdict

class Solution:
    def matchReplacement(self, s, sub, mappings):
        d=defaultdict(set)
        for i,j in mappings:
            d[i].add(j)
        n,m=len(s),len(sub)
        for i in range(n-m+1):
            flag=1
            for x,y in zip(s[i:i+m],sub):
                if x==y or x in d[y]:
                    continue
                else:
                    flag=0
                    break
            if flag:
                return True
        return False
        
        '''
        # TLE
        def check(i,s,sub):
            idx=0
            for j in range(i,i+len(sub)):
                if s[j]==sub[idx] or (sub[idx],s[j]) in d:
                    idx+=1
                else:
                    return False
            return True

        d=[]
        for i,j in mappings:
            d.append((i,j))
        for i in range(len(s)-len(sub)+1):
            if check(i,s,sub):
                return True
        return False
        '''