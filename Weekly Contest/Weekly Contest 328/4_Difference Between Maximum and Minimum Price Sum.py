# 2538. Difference Between Maximum and Minimum Price Sum
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

class Solution:
    def maxOutput(self, n, edges, price):
        '''
        @lru_cache(None)
        def dfs(node,parent):
            val=price[node]
            temp=0
            for nei in adj_list[node]:
                if nei!=parent:
                    temp=max(temp,dfs(nei,node))
            return temp+val

        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        ans=float('-inf')
        for i in range(n):
            x=dfs(i,-1)
            ans=max(ans,x-price[i])
        return ans
        '''

        def dfs(node,parent):
            temp=0
            for nei in adj_list[node]:
                if nei!=parent:
                    temp=max(temp,dfs(nei,node))
            subtree_sum[node]=price[node]+temp
            return subtree_sum[node]
        
        def reroot(node,parent,parent_contribution):
            first_max_val,second_max_val=0,0
            first_max_price,second_max_price=0,0
            for nei in adj_list[node]:
                if nei!=parent:
                    if subtree_sum[nei]>second_max_price:
                        second_max_price=subtree_sum[nei]
                        second_max_val=nei
                    if second_max_price>first_max_price:
                        first_max_price,second_max_price=second_max_price,first_max_price
                        first_max_val,second_max_val=second_max_val,first_max_val
            self.ans=max(self.ans,parent_contribution,first_max_price)
            for nei in adj_list[node]:
                if nei!=parent:
                    if nei!=first_max_val:
                        reroot(nei,node,price[node]+max(parent_contribution,first_max_price))
                    else:
                        reroot(nei,node,price[node]+max(parent_contribution,second_max_price))

        adj_list=[[] for _ in range(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        subtree_sum=[0]*n
        dfs(0,-1)
        self.ans=0
        reroot(0,-1,0)
        return self.ans