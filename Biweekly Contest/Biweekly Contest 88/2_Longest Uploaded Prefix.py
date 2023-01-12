# 2424. Longest Uploaded Prefix
# https://leetcode.com/problems/longest-uploaded-prefix/

'''
class LUPrefix:

    def __init__(self, n: int):
        self.l=[0]*n
        self.prev=0

    def upload(self, video: int) -> None:
        self.l[video-1]=1

    def longest(self) -> int:
        while self.prev<len(self.l) and self.l[self.prev]:
            self.prev+=1
        return self.prev


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
'''

class LUPrefix:

    def __init__(self, n: int):
        self.s=set()
        self.idx=0

    def upload(self, video: int) -> None:
        self.s.add(video)
        while self.idx+1 in self.s:
            self.idx+=1

    def longest(self) -> int:
        return self.idx


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

'''
from sortedcontainers import SortedList
class LUPrefix:

    def __init__(self, n: int):
        self.l=SortedList([i+1 for i in range(n)])
        self.n=n

    def upload(self, video: int) -> None:
        self.l.remove(video)

    def longest(self) -> int:
        return self.l[0]-1 if self.l else self.n

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
'''