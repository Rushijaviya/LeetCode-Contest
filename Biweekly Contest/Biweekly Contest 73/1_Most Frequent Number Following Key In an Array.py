# 2190. Most Frequent Number Following Key In an Array
# https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

class Solution:
    def mostFrequent(self, nums, key):
        idx=nums.index(key)
        d={}
        while True:
            if idx<len(nums)-1:
                d[nums[idx+1]]=d.get(nums[idx+1],0)+1
            nums.pop(idx)
            try:
                idx=nums.index(key)
            except Exception as e:
                break
        maxvalue=max(d.values())
        for i,j in d.items():
            if j==maxvalue:
                return i

        '''
        c = Counter()
        for i, n in enumerate(nums):
            if n == key and i + 1 < len(nums):
                c[nums[i + 1]] += 1
        return c.most_common(1)[0][0]
        '''