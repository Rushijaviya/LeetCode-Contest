# 2663. Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

class Solution:
    def smallestBeautifulString(self, s, k):
        s=list(map(lambda x:ord(x)-97,s))
        idx=len(s)-1
        while idx>=0:
            s[idx]+=1
            if s[idx]==k:
                idx-=1
            elif s[idx] not in s[max(0,idx-2):idx]:
                for j in range(idx+1,len(s)):
                    s[j]=min({0,1,2}-set(s[max(0,j-2):j]))
                return "".join(chr(i+97) for i in s)
        return ""