# 2276. Count Integers in Intervals
# https://leetcode.com/problems/count-integers-in-intervals/

from bisect import bisect_left, bisect_right
from operator import itemgetter

class CountIntervals:

    def __init__(self):
        self.interval=[(-float('inf'),-float('inf')),(float('inf'),float('inf'))]
        self.cov=0

    def add(self, left: int, right: int) -> None:
        interval=self.interval
        left_idx=bisect_left(interval,left-1,key=itemgetter(1))
        right_idx=bisect_right(interval,right+1,key=itemgetter(0))
        left_val=min(interval[left_idx][0],left)
        right_val=max(interval[right_idx-1][1],right)
        common=0
        for i in range(left_idx,right_idx):
            common+=(interval[i][1]-interval[i][0]+1)
        self.cov+=(right_val-left_val+1-common)
        interval[left_idx:right_idx]=[(left_val,right_val)]

    def count(self) -> int:
        return self.cov


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()

'''
from bisect import bisect_left
from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.cov=0
        self.interval=SortedList()

    def add(self, left: int, right: int) -> None:
        idx=bisect_left(self.interval,(left,right))
        while idx<len(self.interval) and self.interval[idx][0]<=right:
            l,r=self.interval.pop(idx)
            right=max(right,r)
            self.cov-=(r-l+1)
        if idx and self.interval[idx-1][1]>=left:
            l,r=self.interval.pop(idx-1)
            self.cov-=(r-l+1)
            left=l
            right=max(right,r)
        self.cov+=(right-left+1)
        self.interval.add((left,right))

    def count(self) -> int:
        return self.cov


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
'''