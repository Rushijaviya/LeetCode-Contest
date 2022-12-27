# 2344. Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

class Solution:
    def minOperations(self, nums, numsDivide):
        '''
        def vaild(x):
            for i in numsDivide:
                if i%x:
                    return False
            return True

        c=Counter(nums)
        nums=list(set(nums))
        nums.sort()
        ans=0
        for num in nums:
            if vaild(num):
                return ans
            ans+=c[num]
        return -1
        '''
        
        '''
        # O(nlogn) - sorting
        def GcdOfTwo(a,b):
            if b==0:
                return a
            return GcdOfTwo(b,a%b)

        def gcd(l):
            temp=l[0]
            for i in l[1:]:
                temp=GcdOfTwo(temp,i)
            return temp
        
        x=gcd(numsDivide)
        nums.sort()
        for idx,value in enumerate(nums):
            if x%value==0:
                return idx
        return -1
        '''
        
        # O(n)
        def GcdOfTwo(a,b):
            if b==0:
                return a
            return GcdOfTwo(b,a%b)

        def gcd(l):
            temp=l[0]
            for i in l[1:]:
                temp=GcdOfTwo(temp,i)
            return temp
        
        x=gcd(numsDivide)
        min_value=float('inf')
        for i in nums:
            if x%i==0:
                min_value=min(min_value,i)
        if min_value==float('inf'):
            return -1
        count=0
        for i in nums:
            if i<min_value:
                count+=1
        return count