# 2262. Total Appeal of A String
# https://leetcode.com/problems/total-appeal-of-a-string/

class Solution:
    def appealSum(self, s):
        curr=0
        ans=0
        prev={}
        for idx,char in enumerate(s):
            curr+=idx-prev.get(char,-1)
            prev[char]=idx
            ans+=curr
        return ans

        '''
        last = defaultdict(lambda: -1)
        res, n = 0, len(s)
        for idx, char in enumerate(s):
            res += (idx - last[char]) * (n - idx)
            last[char] = idx
        return res
        '''