# 2442. Count Number of Distinct Integers After Reverse Operations
# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums):
        '''
        def reverse(num):
            return int(str(num)[::-1].lstrip('0'))

        nums=set(nums)
        pos=set()
        for i in nums:
            pos.add(i)
            pos.add(reverse(i))
        return len(pos)
        '''

        def reverse(num):
            ans=0
            while num>0:
                ans=ans*10+num%10
                num//=10
            return ans

        rev=set()
        nums=set(nums)
        for i in nums:
            rev.add(reverse(i))
        return len(rev.union(nums))