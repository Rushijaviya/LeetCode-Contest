# 2556. Disconnect Path in a Binary Matrix by at Most One Flip
# https://leetcode.com/problems/disconnect-path-in-a-binary-matrix-by-at-most-one-flip/

class Solution:
    def isPossibleToCutPath(self, grid):
        def dfs(i,j):
            if i==m-1 and j==n-1:
                return True
            if 0<=i+1<m and 0<=j<n and grid[i+1][j]==1:
                grid[i+1][j]=0
                if dfs(i+1,j):
                    return True
            if 0<=i<m and 0<=j+1<n and grid[i][j+1]==1:
                grid[i][j+1]=0
                if dfs(i,j+1):
                    return True
            return False

        m,n=len(grid),len(grid[0])
        if grid[0][0]==0 or grid[-1][-1]==0:
            return False
        if not dfs(0,0):
            return True
        grid[0][0]=1
        grid[-1][-1]=1
        return not dfs(0,0)
        
        '''
        def dfs(i,j,visited,path):
            if i==m-1 and j==n-1:
                return True
            if 0<=i+1<m and 0<=j<n and (i+1,j) not in visited and grid[i+1][j]==1:
                visited.add((i+1,j))
                path.add((i+1,j))
                if dfs(i+1,j,visited,path):
                    return True
                path.remove((i+1,j))
            if 0<=i<m and 0<=j+1<n and (i,j+1) not in visited and grid[i][j+1]==1:
                visited.add((i,j+1))
                path.add((i,j+1))
                if dfs(i,j+1,visited,path):
                    return True
                path.remove((i,j+1))
            return False

        m,n=len(grid),len(grid[0])
        if grid[0][0]==0 or grid[-1][-1]==0:
            return False
        
        visited=set()
        path=set()
        visited.add((0,0))
        path.add((0,0))
        res=dfs(0,0,visited,path)
        if not res:
            return True
        for i,j in path:
            grid[i][j]=0
        grid[0][0]=1
        grid[-1][-1]=1
        visited=set()
        visited.add((0,0))
        return not dfs(0,0,visited,path)
        '''
        
        '''
        m,n=len(grid),len(grid[0])
        dp1=[[0]*(n+1) for _ in range(m+1)]
        dp1[1][1]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if grid[i-1][j-1]:
                    dp1[i][j]+=dp1[i-1][j]+dp1[i][j-1]

        dp2=[[0]*(n+1) for _ in range(m+1)]
        dp2[-2][-2]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if grid[i][j]:
                    dp2[i][j]+=dp2[i+1][j]+dp2[i][j+1]
        
        target=dp1[-1][-1]
        for i in range(m):
            for j in range(n):
                if (i!=0 or j!=0) and (i!=m-1 or j!=n-1):
                    if dp1[i+1][j+1]*dp2[i][j]==target:
                        return True
        return False
        '''