# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n, edges):
        '''
        def dfs(i,adj_list,visited,temp):
            visited[i]=1
            temp.append(i)
            for j in adj_list[i]:
                if not visited[j]:
                    dfs(j,adj_list,visited,temp)
            return temp
        
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        visited=[0]*n
        ans=(n*(n-1))//2
        for i in range(n):
            if not visited[i]:
                temp=dfs(i,adj_list,visited,[])
                ans-=((len(temp))*(len(temp)-1))//2
        return ans
        '''

        '''
        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        bfs=[]
        visited=[0]*n
        ans=(n*(n-1))//2
        for i in range(n):
            if not visited[i]:
                temp=[]
                queue=[i]
                visited[i]=1
                while queue:
                    node=queue.pop(0)
                    temp.append(node)
                    for j in adj_list[node]:
                        if not visited[j]:
                            queue.append(j)
                            visited[j]=1
                ans-=((len(temp))*(len(temp)-1))//2
        return ans
        '''

'''
class disjoinset:
    def __init__(self,n):        
        self.parent=[i for i in range(n)]
        self.rank=[0]*n

    def findper(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node] = self.findper(self.parent[node])    # path compression
        return self.parent[node]

    def union(self,x,y):
        x,y=self.findper(x),self.findper(y)
        if self.rank[x]==self.rank[y]:
            self.parent[y]=x
            self.rank[x]+=1
        elif self.rank[x]>self.rank[y]:
            self.parent[y]=x
        else:
            self.parent[x]=y

class Solution:
    def countPairs(self, n, edges):
        obj=disjoinset(n)
        for i,j in edges:
            obj.union(i,j)
        d={}
        for i in range(n):
            x=obj.findper(i)
            d[x]=d.get(x,0)+1
        l=list(d.values())
        firstgroup=l[0]
        ans=0
        for i in range(1,len(l)):
            ans+=(firstgroup*l[i])
            firstgroup+=l[i]
        return ans
'''