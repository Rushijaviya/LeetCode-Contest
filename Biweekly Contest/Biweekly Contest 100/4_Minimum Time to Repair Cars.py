# 2594. Minimum Time to Repair Cars
# https://leetcode.com/problems/minimum-time-to-repair-cars/

from math import sqrt

class Solution:
    def repairCars(self, ranks, cars):

        def valid(time):
            count=0
            for rank in ranks:
                count+=int(sqrt(time/rank))
            return count>=cars

        start=1
        end=100*cars*cars   # max(ranks)*cars*cars
        while start<=end:
            mid=(start+end)//2
            if valid(mid):
                end=mid-1
            else:
                start=mid+1
        return end+1

        # return bisect_left(range(100*cars*cars), cars, key=lambda x: sum(int(sqrt(x / rank)) for rank in ranks))