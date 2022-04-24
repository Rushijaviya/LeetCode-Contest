# 2250. Count Number of Rectangles Containing Each Point
# https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

from collections import defaultdict

class Solution:
    def countRectangles(self, rectangles, points):

        def binsearch(l,target):
            start,end=0,len(l)-1
            ans=len(l)
            while start<=end:
                mid=(start+end)//2
                if l[mid]>=target:
                    ans=mid
                    end=mid-1
                else:
                    start=mid+1
            return ans

        d=defaultdict(list)
        for l,h in rectangles:
            d[h].append(l)
        for i,j in d.items():
            j.sort()

        ans=[]
        for x,y in points:
            count=0
            for j in range(y,101):
                if j in d:
                    count+=(len(d[j])-binsearch(d[j],x))
            ans.append(count)
        return ans 