# 2605. Form Smallest Number From Two Digit Arrays
# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

class Solution:
    def minNumber(self, nums1, nums2):
        z=set(nums1).intersection(set(nums2))
        if z:
            return min(z)
        x,y=min(nums1),min(nums2)
        return x*10+y if x<y else y*10+x
        
        '''
        arr=[0]*10
        for i in nums1:
            arr[i]+=1
        for i in nums2:
            arr[i]+=1
        for i in range(10):
            if arr[i]==2:
                return i
        x,y=min(nums1),min(nums2)
        return min(x,y)*10+max(x,y)
        '''