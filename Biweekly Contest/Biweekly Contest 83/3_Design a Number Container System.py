# 2349. Design a Number Container System
# https://leetcode.com/problems/design-a-number-container-system/

'''
# TLE
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.nums=defaultdict(list)
        self.idx={}

    def change(self, index: int, number: int) -> None:
        if index in self.idx:
            val=self.idx[index]
            self.nums[val].remove(index)
        self.nums[number].append(index)
        self.idx[index]=number

    def find(self, number: int) -> int:
        l=self.nums[number]
        if not l:
            return -1
        l.sort()
        return l[0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
'''

'''
from collections import defaultdict
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.nums=defaultdict(SortedList)
        self.idx={}

    def change(self, index: int, number: int) -> None:
        if index in self.idx:
            val=self.idx[index]
            self.nums[val].remove(index)
        self.nums[number].add(index)
        self.idx[index]=number

    def find(self, number: int) -> int:
        l=self.nums[number]
        if not l:
            return -1
        return l[0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
'''

from collections import defaultdict
from heapq import heappop, heappush

class NumberContainers:

    def __init__(self):
        self.nums=defaultdict(list)
        self.idx={}
        self.s=defaultdict(set)

    def change(self, index: int, number: int) -> None:
        if index in self.idx:
            val=self.idx[index]
            self.s[val].remove(index)
        self.s[number].add(index)
        self.idx[index]=number
        heappush(self.nums[number],index)

    def find(self, number: int) -> int:
        while self.nums[number] and self.nums[number][0] not in self.s[number]:
            heappop(self.nums[number])
        return self.nums[number][0] if self.nums[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)