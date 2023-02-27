# 2570. Merge Two 2D Arrays by Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution:
    def mergeArrays(self, nums1, nums2):
        '''
        d={}
        for i,j in nums1:
            d[i]=j
        for i,j in nums2:
            if i not in d:
                d[i]=0
            d[i]+=j
        ans=[[i,j] for i,j in d.items()]
        ans.sort()
        return ans
        '''

        ans=[]
        i=j=0
        while i<len(nums1) and j<len(nums2):
            min_val=min(nums1[i][0],nums2[j][0])
            ans.append([min_val,0])
            if nums1[i][0]==min_val:
                ans[-1][-1]+=nums1[i][1]
                i+=1
            if nums2[j][0]==min_val:
                ans[-1][-1]+=nums2[j][1]
                j+=1
        if i<len(nums1):
            ans+=nums1[i:]
        if j<len(nums2):
            ans+=nums2[j:]
        return ans