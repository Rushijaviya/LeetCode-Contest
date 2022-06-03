# 2285. Maximum Total Importance of Roads
# https://leetcode.com/problems/maximum-total-importance-of-roads/

class Solution:
    def maximumImportance(self, n, roads):
        count=[0]*n
        for i,j in roads:
            count[i]+=1
            count[j]+=1
        count.sort()
        ans=0
        for i in range(n):
            ans+=(count[i]*(i+1))
        return ans
        
        '''
        adj_list=[[]*n for _ in range(n)]
        for i in range(n):
            adj_list[i].append(str(i))
        for i,j in roads:
            adj_list[i].append(j)
            adj_list[j].append(i)
        adj_list.sort(key=lambda x:len(x))
        value={}
        for i in range(n):
            value[int(adj_list[i][0])]=i+1
        ans=0
        for i,j in roads:
            ans+=value[i]
            ans+=value[j]
        return ans
        '''