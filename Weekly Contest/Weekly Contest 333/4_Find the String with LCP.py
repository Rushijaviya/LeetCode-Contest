# 2573. Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/

class Solution:
    def findTheString(self, lcp):
        '''
        # TLE
        def common(r,c):
            count=0
            while r<n and c<n:
                if ans[r]==ans[c]:
                    count+=1
                    r+=1
                    c+=1
                else:
                    break
            return count
        
        n=len(lcp)
        ans="a"
        first=lcp[0]
        if first[0]!=n:
            return ""
        char='b'
        i=1
        while i<n:
            if first[i]==0:
                for j in range(1,i):
                    if lcp[j][i]!=0:
                        ans+=ans[j]
                        i+=1
                        break
                else:
                    if char=='{':
                        return ""
                    ans+=char
                    char=chr(ord(char)+1)
                    i+=1
            else:
                j=0
                for _ in range(first[i]):
                    ans+=ans[j]
                    j+=1
                i+=first[i]
        for i in range(n):
            for j in range(n):
                if common(i,j)!=lcp[i][j]:
                    return ""
        return ans
        '''
        
        n=len(lcp)
        ans='a'
        char='b'
        idx=1
        while idx<n:
            if lcp[0][idx]==0:
                for j in range(1,idx):
                    if lcp[j][idx]:
                        ans+=ans[j]
                        idx+=1
                        break
                else:
                    if char=='{':
                        return ""
                    ans+=char
                    char=chr(ord(char)+1)
                    idx+=1
            else:
                j=0
                for _ in range(lcp[0][idx]):
                    ans+=ans[j]
                    j+=1
                idx+=lcp[0][idx]
        for i in range(n):
            for j in range(n):
                temp=lcp[i+1][j+1] if i+1<n and j+1<n else 0
                temp=temp+1 if (ans[i]==ans[j]) else 0
                if temp!=lcp[i][j]:
                    return ""
        return ans