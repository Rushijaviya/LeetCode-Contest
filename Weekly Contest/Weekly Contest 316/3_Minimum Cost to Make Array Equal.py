# 2448. Minimum Cost to Make Array Equal
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/

class Solution:
    def minCost(self, nums, cost):
        '''
        s=set(nums)
        n=len(nums)
        ans=float('inf')
        for num in s:
            total_cost=0
            for idx in range(n):
                total_cost+=abs(num-nums[idx])*cost[idx]
            ans=min(ans,total_cost)
        return ans
        '''
        
        '''
        def f(num):
            return sum(abs(num-nums[i])*cost[i] for i in range(len(nums)))

        start=min(nums)
        end=max(nums)
        ans=f(start)
        while start<=end:
            mid=(start+end)//2
            x,y=f(mid),f(mid+1)
            ans=min(x,y)
            if x<=y:
                end=mid-1
            else:
                start=mid+1
        return ans
        '''
        
        arr=sorted(list(zip(nums,cost)))
        total_cost=sum(cost)
        count=0
        for i,j in arr:
            count+=j
            if count>total_cost//2:
                meidan=i
                break
        return sum(abs(meidan-nums[i])*cost[i] for i in range(len(nums)))
        
        '''
        arr=sorted(list(zip(nums,cost)))
        nums=[]
        cost=[]
        for i,j in arr:
            nums.append(i)
            cost.append(j)
        n=len(nums)

        lefttoright=[0]*n
        curr=cost[0]
        for i in range(1,n):
            lefttoright[i]=lefttoright[i-1]+(nums[i]-nums[i-1])*curr
            curr+=cost[i]
        
        curr=cost[-1]
        righttoleft=[0]*n
        for i in range(n-2,-1,-1):
            righttoleft[i]=righttoleft[i+1]+(nums[i+1]-nums[i])*curr
            curr+=cost[i]
        
        return min(lefttoright[i]+righttoleft[i] for i in range(n))
        '''