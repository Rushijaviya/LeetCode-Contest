# 2354. Number of Excellent Pairs
# https://leetcode.com/problems/number-of-excellent-pairs/

class Solution:
    def countExcellentPairs(self, nums, k):
        '''
        s=set()
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if ((bin(nums[i]&nums[j])).count('1')+(bin(nums[i]|nums[j])).count('1'))>=k:
                    s.add((nums[i],nums[j]))
                    s.add((nums[j],nums[i]))
        for i in nums:
            if bin(i).count('1')>=(k+1)//2:
                s.add((i,i))
        return len(s)
        '''
        
        '''
        nums=set(nums)
        c=Counter(map(lambda x:bin(x).count('1'),nums))
        ans=0
        for k1 in c:
            for k2 in c:
                if k1+k2>=k:
                    ans+=(c[k1]*c[k2])
        return ans
        '''

        nums=set(nums)
        l=[]
        for i in nums:
            l.append(i.bit_count())
        l.sort()
        n=len(l)
        j=n-1
        ans=0
        for i in range(n):
            while j>=0 and l[i]+l[j]>=k:
                j-=1
            ans+=(n-j-1)
        return ans