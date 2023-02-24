# 2558. Take Gifts From the Richest Pile
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

from heapq import heapify, heappushpop
from math import floor, sqrt
from sortedcontainers import SortedList

class Solution:
    def pickGifts(self, gifts, k):
        '''
        gifts=SortedList(gifts)
        for _ in range(k):
            x=gifts.pop()
            gifts.add(floor(sqrt(x)))
        return sum(gifts)
        '''

        gifts=list(map(lambda x:-x,gifts))
        heapify(gifts)
        for _ in range(k):
            heappushpop(gifts,-floor(sqrt(-gifts[0])))
        return -sum(gifts)