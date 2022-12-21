# 2321. Maximum Score Of Spliced Array
# https://leetcode.com/problems/maximum-score-of-spliced-array/

class Solution:
    def maximumsSplicedArray(self, nums1, nums2):
        '''
        # TLE
        n=len(nums1)
        pref1=[0]*n
        pref2=[0]*n
        pref1[0]=nums1[0]
        for i in range(1,n):
            pref1[i]=pref1[i-1]+nums1[i]
        pref2[0]=nums2[0]
        for i in range(1,n):
            pref2[i]=pref2[i-1]+nums2[i]
        sum1=sum(nums1)
        sum2=sum(nums2)
        ans=max(sum1,sum2)        
        for i in range(n):
            for j in range(i,n):
                x=(pref1[j]-(pref1[i-1]) if i>0 else 0)
                y=(pref2[j]-(pref2[i-1]) if i>0 else 0)
                temp1=sum1-x+y
                temp2=sum2-y+x
                ans=max(ans,temp1,temp2)
        return ans
        '''
        
        '''
        def kadane(arr):
            ans=float('-inf')
            s=0
            for i in arr:
                s=max(i,s+i)
                ans=max(ans,s)
            return ans

        n=len(nums1)
        temp1=[]
        temp2=[]
        for i in range(n):
            temp1.append(nums1[i]-nums2[i])
            temp2.append(nums2[i]-nums1[i])
        total_sum1,total_sum2=sum(nums1),sum(nums2)
        sum1=kadane(temp1)
        sum2=kadane(temp2)
        return max(total_sum1,total_sum2,total_sum1+sum2,total_sum2+sum1)
        '''

        n=len(nums1)
        total_sum1,total_sum2=sum(nums1),sum(nums2)
        ans1,ans2=float('-inf'),float('-inf')
        s1,s2=0,0
        for i in range(n):
            x=nums1[i]-nums2[i]
            s1=max(x,s1+x)
            s2=max(-x,s2-x)
            ans1=max(ans1,s1)
            ans2=max(ans2,s2)
        return max(total_sum1,total_sum2,total_sum1+ans2,total_sum2+ans1)