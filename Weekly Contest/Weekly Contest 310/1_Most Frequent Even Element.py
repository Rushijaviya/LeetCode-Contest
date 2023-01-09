# 2404. Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/

from collections import defaultdict

class Solution:
    def mostFrequentEven(self, nums):
        '''
        c=Counter(nums)
        temp=[(i,j) for i,j in c.items() if i%2==0]
        if not temp:
            return -1
        temp.sort(key=lambda x:(-x[1],x[0]))
        return temp[0][0]   
        '''

        '''
        return min(multimode(x for x in nums if not x % 2), default=-1)
        '''

        d=defaultdict(int)
        ans=-1
        for i in nums:
            if i%2==0:
                d[i]+=1
                if d[i]>d[ans]:
                    ans=i
                elif d[i]==d[ans]:
                    ans=min(ans,i)
        return ans