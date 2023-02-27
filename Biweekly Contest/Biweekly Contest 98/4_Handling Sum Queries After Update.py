# 2569. Handling Sum Queries After Update
# https://leetcode.com/problems/handling-sum-queries-after-update/

class Solution:
    def handleQuery(self, nums1, nums2, queries):
        '''
        # TLE
        ans=[]
        for case,left,right in queries:
            if case==1:
                nums1[left:right+1]=list(map(lambda x:1-x,nums1[left:right+1]))
            elif case==2:
                for idx in range(len(nums2)):
                    nums2[idx]+=(nums1[idx]*left)
            else:
                ans.append(sum(nums2))
        return ans
        '''
        
        '''
        # TLE
        ans=[]
        total_sum=sum(nums2)
        count=nums1.count(1)
        for case,left,right in queries:
            if case==1:
                for idx in range(left,right+1):
                    if nums1[idx]==1:
                        count-=1
                        nums1[idx]=0
                    else:
                        count+=1
                        nums1[idx]=1
            elif case==2:
                total_sum+=(count*left)
            else:
                ans.append(total_sum)
        return ans
        '''

        ans=[]
        nums1=int("".join(map(str,nums1[::-1])),2)
        total_sum=sum(nums2)
        for case,left,right in queries:
            if case==1:
                a=(1<<left)-1
                b=(1<<(right+1))-1
                nums1=nums1^a^b
            elif case==2:
                total_sum+=(nums1.bit_count()*left)
            else:
                ans.append(total_sum)
        return ans