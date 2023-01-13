# 2426. Number of Pairs Satisfying Inequality
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):

        def merge(start,end):
            count=0
            if start<end:
                mid=(start+end)//2
                count+=merge(start,mid)
                count+=merge(mid+1,end)
                left=start
                for right in range(mid+1,end+1):
                    while left<=mid and nums[left]<=(nums[right]+diff):
                        count+=(end-right+1)
                        left+=1
                nums[start:end+1]=sorted(nums[start:end+1])
            return count

        n=len(nums1)
        nums=[]
        for i in range(n):
            nums.append(nums1[i]-nums2[i])
        return merge(0,n-1)