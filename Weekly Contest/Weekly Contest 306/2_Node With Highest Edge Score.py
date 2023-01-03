# 2374. Node With Highest Edge Score
# https://leetcode.com/problems/node-with-highest-edge-score/

class Solution:
    def edgeScore(self, edges):
        '''
        d=defaultdict(int)
        ans=[-1,-1]
        for i in range(len(edges)):
            d[edges[i]]+=i
            if ans[1]<d[edges[i]]:
                ans=[edges[i],d[edges[i]]]
            elif ans[1]==d[edges[i]]:
                ans[0]=min(ans[0],edges[i])
        return ans[0]
        '''
        
        n=len(edges)
        arr=[0]*n
        for i in range(n):
            arr[edges[i]]+=i
        return arr.index(max(arr))