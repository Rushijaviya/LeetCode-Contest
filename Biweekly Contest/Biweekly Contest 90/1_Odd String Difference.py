# 2451. Odd String Difference
# https://leetcode.com/problems/odd-string-difference/

from collections import defaultdict

class Solution:
    def oddString(self, words):
        '''
        def finddiff(s):
            return tuple([ord(s[i])-ord(s[i-1]) for i in range(1,len(s))])

        d={}
        for word in words:
            x=finddiff(word)
            if x not in d:
                d[x]=[]
            d[x].append(word)
        
        for i in d:
            if len(d[i])==1:
                return d[i][0]
        '''

        for idx in range(1,len(words[0])):
            d=defaultdict(list)
            for j in range(len(words)):
                if len(d[ord(words[j][idx])-ord(words[j][idx-1])])<2:
                    d[ord(words[j][idx])-ord(words[j][idx-1])].append(j)
            if len(d)==2:
                for i in d:
                    if len(d[i])==1:
                        return words[d[i][0]]