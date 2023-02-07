# 2502. Design Memory Allocator
# https://leetcode.com/problems/design-memory-allocator/

from collections import defaultdict
from sortedcontainers import SortedDict

'''
class Allocator:

    def __init__(self, n: int):
        self.arr=[-1]*n
        self.available=n

    def allocate(self, size: int, mID: int) -> int:
        if self.available==0:
            return -1
        left=0
        for right in range(len(self.arr)):
            if self.arr[right]!=-1:
                left=right+1
            elif right-left+1==size:
                self.arr[left:right+1]=[mID]*size
                self.available-=size
                return left
        return -1

    def free(self, mID: int) -> int:
        if self.available==len(self.arr):
            return 0
        prev=self.available
        for i in range(len(self.arr)):
            if self.arr[i]==mID:
                self.arr[i]=-1
                self.available+=1
        return self.available-prev


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
'''

class Allocator:

    def __init__(self, n: int):
        self.alloct=defaultdict(list)
        self.available=SortedDict({0:n})
        
    def allocate(self, size: int, mID: int) -> int:
        for startidx,freesize in self.available.items():
            if freesize>=size:
                del self.available[startidx]
                self.alloct[mID].append((startidx,size))
                if freesize>size:
                    self.available[startidx+size]=freesize-size
                return startidx
        return -1

    def combine(self,s1,s2):
        if s1+self.available[s1]==s2:
            self.available[s1]+=self.available[s2]
            del self.available[s2]

    def free(self, mID: int) -> int:
        if mID not in self.alloct:
            return 0
        count=0
        for idx,size in self.alloct[mID]:
            count+=size
            self.available[idx]=size
            keys=self.available.keys()
            i=self.available.bisect_left(idx)
            if i+1<len(self.available):
                self.combine(idx,keys[i+1])
            if i-1>=0:
                self.combine(keys[i-1],idx)
        del self.alloct[mID]
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)