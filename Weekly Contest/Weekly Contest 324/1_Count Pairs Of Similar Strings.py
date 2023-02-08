# 2506. Count Pairs Of Similar Strings
# https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution:
    def similarPairs(self, words):
        '''
        count=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if set(words[i])==set(words[j]):
                    count+=1
        return count
        '''

        n=len(words)
        dp=[0]*n
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if set(words[j])==set(words[i]):
                    dp[i]=dp[j]+1
                    break
        return sum(dp)
        
        '''
        words=[tuple(sorted(set(word))) for word in words]
        c=Counter(words)
        return sum((n*(n-1))//2 for n in c.values())
        '''