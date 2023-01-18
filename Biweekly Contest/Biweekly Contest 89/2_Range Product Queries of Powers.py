# 2438. Range Product Queries of Powers
# https://leetcode.com/problems/range-product-queries-of-powers/

class Solution:
    def productQueries(self, n, queries):
        def findbin(num):
            res=[]
            for i in range(32):
                if num&(1<<i):
                    res.append(1<<i)
            return res

        arr=findbin(n)
        pref=[1,arr[0]]
        for i in arr[1:]:
            pref.append(pref[-1]*i)
        ans=[]
        for i,j in queries:
            ans.append((pref[j+1]//pref[i])%(10**9+7))
        return ans