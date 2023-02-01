# 2483. Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        '''
        n=len(customers)
        ans=[[0,0] for _ in range(n+1)]
        for i in range(n):
            if customers[i]=='Y':
                ans[i][0]+=1
            else:
                ans[i+1][1]+=1
        for i in range(1,n+1):
            ans[i][1]+=ans[i-1][1]
        for i in range(n-1,-1,-1):
            ans[i][0]+=ans[i+1][0]
        ans=list(map(lambda x:x[0]+x[1],ans))
        return ans.index(min(ans))
        '''
        
        visited_Y=0
        visited_N=0
        total_Y=0
        total_N=0
        for i in customers:
            if i=='Y':
                total_Y+=1
            else:
                total_N+=1
        ans=[float('inf'),float('inf')]
        for i in range(len(customers)+1):
            temp=visited_N+total_Y-visited_Y
            if temp<ans[0]:
                ans[0]=temp
                ans[1]=i
            if i==len(customers):
                continue
            if customers[i]=='Y':
                visited_Y+=1
            else:
                visited_N+=1
        return ans[1]
        
        '''
        count=customers.count('Y')
        ans=[float('inf'),float('inf')]
        for i in range(len(customers)+1):
            if count<ans[0]:
                ans[0]=count
                ans[1]=i
            if i==len(customers):
                continue
            if customers[i]=='Y':
                count-=1
            else:
                count+=1
        return ans[1]
        '''
        
        '''
        count=0
        ans=[0,-1]
        for i in range(len(customers)):
            if customers[i]=='Y':
                count+=1
            else:
                count-=1
            if count>ans[0]:
                ans[0]=count
                ans[1]=i
        return ans[1]+1
        '''