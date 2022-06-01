# 2272. Substring With Largest Variance
# https://leetcode.com/problems/substring-with-largest-variance/

class Solution:
    def largestVariance(self, s):
        '''
        # TLE
        n=len(s)
        ans=0
        for i in range(n):
            d={}
            for j in range(i,n):
                d[s[j]]=d.get(s[j],0)+1
                temp=sorted(d.values(),key=lambda x:x)
                ans=max(ans,temp[-1]-temp[0])
        return ans
        '''

        '''
        ans=0
        l=list(set(s))
        n=len(l)
        for i in range(n):
            for j in range(i+1,n):
                c1,c2=l[i],l[j]
                diff=0
                max_diff=min_diff=0
                last_c1_diff=last_c2_diff=0
                meet_c1=meet_c2=False
                for c in s:
                    if c1==c:
                        meet_c1=True
                        diff+=1
                        max_diff=max(max_diff,last_c1_diff)
                        last_c1_diff=diff
                    elif c2==c:
                        meet_c2=True
                        diff-=1
                        min_diff=min(min_diff,last_c2_diff)
                        last_c2_diff=diff
                    else:
                        continue
                    if meet_c1 and meet_c2:
                        ans=max(diff-min_diff,max_diff-diff,ans)
        return ans
        '''
        
        # kadanes algorithm
        def maxSubArray(nums):
            ans=-float('inf')
            runningsum=0
            seen=False
            for x in nums:
                if x<0:
                    seen=True
                runningsum+=x
                if seen:
                    ans=max(ans,runningsum)
                else:
                    ans=max(ans,runningsum-1)
                if runningsum<0:
                    runningsum=0
                    seen=False
            return ans

        a=""
        for i in s:
            if i not in a:
                a+=i
        n=len(s)
        m=len(a)
        ans=0
        for i in range(m):
            for j in range(i+1,m):
                x,y=a[i],a[j]
                arr=[]
                for k in range(n):
                    if s[k]!=x and s[k]!=y:
                        continue
                    elif s[k]==x:
                        arr.append(1)
                    else:
                        arr.append(-1)
                ans=max(ans,maxSubArray(arr),maxSubArray([-i for i in arr]))
        return ans