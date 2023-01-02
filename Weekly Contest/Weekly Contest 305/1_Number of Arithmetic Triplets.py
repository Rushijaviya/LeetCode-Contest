# 2367. Number of Arithmetic Triplets
# https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums, diff: int) -> int:
        '''
        d=defaultdict(int)
        count=0
        for i in nums:
            if i-diff in d and i-2*diff in d:
                count+=(d[i-diff]*d[i-2*diff])
            d[i]+=1
        return count
        '''

        arr=[0]*201
        count=0
        for i in nums:
            if i-2*diff>=0:
                count+=(arr[i-diff] and arr[i-2*diff])
            arr[i]=1
        return count