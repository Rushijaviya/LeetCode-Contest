# 2217. Find Palindrome With Fixed Length
# https://leetcode.com/problems/find-palindrome-with-fixed-length/

class Solution:
    def kthPalindrome(self, queries, x):
        base=10**((x-1)//2)
        ans=[base+q-1 for q in queries]
        for i,j in enumerate(ans):
            j=str(j)+str(j)[-1-x%2::-1]
            ans[i]=int(j) if len(j)==x else -1
        return ans
        
        '''
        start,end=10**((x+1)//2-1),10**((x+1)//2)
        ans=[]
        for q in queries:
            if start+q>end:
                ans.append(-1)
                continue
            firstpart=str(int(start+q-1))
            secondpart=firstpart[::-1]
            secondpart=secondpart[x%2:]
            ans.append(int(firstpart+secondpart))
        return ans
        '''