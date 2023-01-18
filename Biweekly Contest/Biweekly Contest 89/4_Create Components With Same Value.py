# 2440. Create Components With Same Value
# https://leetcode.com/problems/create-components-with-same-value/

class Solution:
    def componentValue(self, nums, edges):

        def vaild(target):
            d=degree[:]
            values=nums[:]
            q=queue[:]
            while q:
                node=q.pop(0)
                if values[node]>target:
                    return False
                d[node]=0
                for nei in adj_list[node]:
                    if values[node]!=target:
                        values[nei]+=values[node]
                    d[nei]-=1
                    if d[nei]==0:
                        return values[nei]==target
                    if d[nei]==1:
                        q.append(nei)
            return False
            

        n=len(nums)
        adj_list=[[] for _ in range(n)]
        degree=[0]*n
        for i,j in edges:
            degree[i]+=1
            degree[j]+=1
            adj_list[i].append(j)
            adj_list[j].append(i)
        queue=[]
        for i in range(n):
            if degree[i]==1:
                queue.append(i)

        limit=sum(nums)
        for i in range(min(nums),limit):
            if limit%i==0 and vaild(i):
                return limit//i-1
        return 0