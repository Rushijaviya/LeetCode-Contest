# 2370. Longest Ideal Subsequence
# https://leetcode.com/problems/longest-ideal-subsequence/

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        '''
        def topologicalSortUtil(current, adj, visited, stk):
            visited[current] = True
            for i in range(len(adj[current])):
                if(visited[adj[current][i][0]] == False):
                    topologicalSortUtil(adj[current][i][0], adj, visited, stk)
            stk.append(current)

        def topologicalSort(adj):
            n = len(adj)
            visited = [False for i in range(n)]
            stk = []
            for i in range(n):
                if(visited[i] == False):
                    topologicalSortUtil(i, adj, visited, stk)
            result = []
            while(len(stk) > 0):
                result.append(stk[-1])
                stk.pop()
            return result
        
        n=len(s)
        s=[ord(i)-97 for i in s]
        adj_list=[[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if abs(s[j]-s[i])<=k:
                    adj_list[i].append([j,1])
        
        order = topologicalSort(adj_list)
        ans=0
        visited=[0]*n
        for pp in range(n):
            if visited[pp]:
                continue
            maxDistances = [-1 for i in range(n)]
            src=pp
            maxDistances[src] = 0
            for i in range(n):
                current = order[i]
                if(maxDistances[current] == -1):
                    continue
                visited[i]=1
                for j in range(len(adj_list[current])):
                    neighbor = adj_list[current][j][0]
                    maxDistances[neighbor] = max(
                        maxDistances[neighbor], maxDistances[current] + adj_list[current][j][1])
            ans=max(ans,max(maxDistances)+1)
        return ans
        '''

        '''
        @lru_cache(None)
        def dp(idx,prev):
            if idx==n:
                return 0
            ans=0
            if prev==-1 or abs(ord(s[prev])-ord(s[idx]))<=k:
                ans=max(ans,1+dp(idx+1,idx))
            ans=max(ans,dp(idx+1,prev))
            return ans

        n=len(s)
        return dp(0,-1)
        '''

        dp=[0]*26
        for char in s:
            idx=ord(char)-ord('a')
            dp[idx]=max(dp[max(0,idx-k):min(26,idx+k+1)])+1
        return max(dp)