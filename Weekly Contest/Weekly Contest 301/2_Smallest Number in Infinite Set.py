# 2336. Smallest Number in Infinite Set
# https://leetcode.com/problems/smallest-number-in-infinite-set/

'''
class SmallestInfiniteSet:

    def __init__(self):
        self.l=[i+1 for i in range(1000)]
        self.l=set(self.l)

    def popSmallest(self) -> int:
        m=min(self.l)
        self.l.remove(m)
        return m

    def addBack(self, num: int) -> None:
        if num not in self.l:
            self.l.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
'''

'''
from sortedcontainers import SortedSet
class SmallestInfiniteSet:

    def __init__(self):
        self.s=SortedSet(i+1 for i in range(1000))

    def popSmallest(self) -> int:
        return self.s.pop(0)

    def addBack(self, num: int) -> None:
        self.s.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
'''

class SmallestInfiniteSet:

    def __init__(self):
        self.removed=set()

    def popSmallest(self) -> int:
        start=1
        while True:
            if start not in self.removed:
                self.removed.add(start)
                return start
            start+=1

    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)