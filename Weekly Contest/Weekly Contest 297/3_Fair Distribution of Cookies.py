# 2305. Fair Distribution of Cookies
# https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies, k):
        ans=float('inf')
        fair=[0]*k

        def dp(i):
            nonlocal ans,fair
            if i==len(cookies):
                ans=min(ans,max(fair))
                return
            if ans<=max(fair):
                return 
            for j in range(k):
                fair[j]+=cookies[i]
                dp(i+1)
                fair[j]-=cookies[i]

        dp(0)
        return ans