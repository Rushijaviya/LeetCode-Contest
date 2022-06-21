# 2306. Naming a Company
# https://leetcode.com/problems/naming-a-company/

from collections import defaultdict

class Solution:
    def distinctNames(self, ideas):
        l=[set() for _ in range(26)]
        for i in ideas:
            l[ord(i[0])-97].add(i[1:])
        ans=0
        for i in range(25):
            for j in range(i+1,26):
                common=len(l[i]&l[j])
                ans+=(2*(len(l[i])-common)*(len(l[j])-common))
        return ans
        
        '''
        l=defaultdict(set)
        for i in ideas:
            l[i[0]].add(i[1:])
        ans=0
        for i,x in l.items():
            for j,y in l.items():
                if i>=j:
                    continue
                common=len(x&y)
                ans+=((len(x)-common)*(len(y)-common))
        return 2*ans
        '''