# 2251. Number of Flowers in Full Bloom
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

class Solution:
    def fullBloomFlowers(self, flowers, persons):

        def started(l,target):
            left,right=0,len(l)-1
            while left<=right:
                mid=(left+right)//2
                if l[mid]>target:
                    right=mid-1
                else:
                    left=mid+1
            return left

        def ended(l,target):
            left,right=0,len(l)-1
            while left<=right:
                mid=(left+right)//2
                if l[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            return left

        start=[]
        end=[]
        for i,j in flowers:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        ans=[]
        for per in persons:
            ans.append(started(start,per)-ended(end,per))
        return ans