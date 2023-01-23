# 2453. Destroy Sequential Targets
# https://leetcode.com/problems/destroy-sequential-targets/

class Solution:
    def destroyTargets(self, nums, space):
        '''
        def fun(tar):
            res=0
            for j in c:
                if (j-tar)%space==0:
                    res+=c[j]
            return res
        
        ans=[-1,-1]
        c=Counter(nums)
        for num in c:
            count=fun(num)
            if ans[0]<count:
                ans=[count,num]
            elif ans[0]==count:
                ans[1]=min(ans[1],num)
        return ans[1]
        '''
        
        '''
        arr=[]
        for num in nums:
            arr.append(num%space)
        c=Counter(arr)
        m=max(c.values())
        ans=float('inf')
        for num in nums:
            if c[num%space]==m:
                ans=min(ans,num)
        return ans
        '''

        d={}
        ans=[-1,-1]
        for num in nums:
            if num%space not in d:
                d[num%space]=[0,num]
            d[num%space]=[d[num%space][0]+1,min(num,d[num%space][1])]
            if d[num%space][0]>ans[0]:
                ans=[d[num%space][0],d[num%space][1]]
            elif d[num%space][0]==ans[0]:
                ans[1]=min(ans[1],d[num%space][1])
        return ans[1]