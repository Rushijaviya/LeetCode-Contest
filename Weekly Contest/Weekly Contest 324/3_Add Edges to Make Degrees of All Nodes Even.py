# 2508. Add Edges to Make Degrees of All Nodes Even
# https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

class Solution:
    def isPossible(self, n, edges):
        '''
        # TLE
        def rec(idx,step,odd):
            if odd==0:
                return True
            if idx==n or step==0:
                return False
            temp=False
            if degree[idx]%2:
                for i in range(n):
                    if i not in adj_list[idx] and i!=idx:
                        adj_list[idx].add(i)
                        adj_list[i].add(idx)
                        degree[i]+=1
                        degree[idx]+=1
                        if degree[idx]%2:
                            odd+=1
                        else:
                            odd-=1
                        if degree[i]%2:
                            odd+=1
                        else:
                            odd-=1
                        temp=temp or rec(idx+1,step-1,odd)
                        if temp:
                            return True
                        adj_list[idx].remove(i)
                        adj_list[i].remove(idx)
                        degree[idx]-=1
                        degree[i]-=1
                        if degree[idx]%2:
                            odd+=1
                        else:
                            odd-=1
                        if degree[i]%2:
                            odd+=1
                        else:
                            odd-=1
            temp=temp or rec(idx+1,step,odd)
            return temp

        adj_list=[set() for _ in range(n)]
        degree=[0]*n
        for i,j in edges:
            adj_list[i-1].add(j-1)
            adj_list[j-1].add(i-1)
            degree[i-1]+=1
            degree[j-1]+=1
        odd=0
        for i in degree:
            if i%2:
                odd+=1
        return rec(0,2,odd)
        '''

        adj_list=[set() for _ in range(n)]
        degree=[0]*n
        for i,j in edges:
            degree[i-1]+=1
            degree[j-1]+=1
            adj_list[i-1].add(j-1)
            adj_list[j-1].add(i-1)
        odd_count=0
        odd_list=[]
        for i in range(n):
            if degree[i]%2:
                odd_count+=1
                odd_list.append(i)
        if odd_count==0:
            return True
        elif odd_count==2:
            if odd_list[0] not in adj_list[odd_list[1]]:
                return True
            for i in range(n):
                if i not in adj_list[odd_list[1]] and i not in adj_list[odd_list[0]]:
                    return True
        elif odd_count==4:
            a,b,c,d=odd_list[0],odd_list[1],odd_list[2],odd_list[3]
            if (a not in adj_list[b] and c not in adj_list[d]) or (a not in adj_list[c] and b not in adj_list[d]) or (a not in adj_list[d] and b not in adj_list[c]):
                return True
        return False