# 2399. Check Distances Between Same Letters
# https://leetcode.com/problems/check-distances-between-same-letters/

class Solution:
    def checkDistances(self, s, distance):
        '''
        visited=set()
        for i in range(len(s)):
            if s[i] not in visited and (i+1+distance[ord(s[i])-97]>=len(s) or s[i+1+distance[ord(s[i])-97]]!=s[i]):
                return False
            visited.add(s[i])
        return True
        '''

        d={}
        for i in range(len(s)):
            if s[i] in d:
                if i-d[s[i]]-1!=distance[ord(s[i])-97]:
                    return False
            else:
                d[s[i]]=i
        return True