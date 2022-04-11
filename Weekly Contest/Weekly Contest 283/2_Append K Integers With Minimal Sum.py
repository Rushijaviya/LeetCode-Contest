# 2195. Append K Integers With Minimal Sum
# https://leetcode.com/problems/append-k-integers-with-minimal-sum/

class Solution:
    def minimalKSum(self, nums, k):
        n=len(nums)
        curr=prev=0   # intialize both curr and prev  
        nums.sort()    # sort the nums
        sum=0     
        for i in range(n):
            curr=nums[i]     # make curr equal to prev
            diff=curr-(prev+1)    # find if there is any numbers in (prev,curr)
            if diff<=0:      # if no then update prev and continue 
                prev=curr
                continue
            if diff>k:       # if yes then if number between (prev,curr) is more then k 
                diff=k   # then we will consider first k numbers only
                curr=prev+1+k # update curr to last number that we will add to use formula 1 of A.P.
            sum+=(diff*(curr+prev)//2)  # formula 1 of A.P.
            prev=curr  # update prev to curr
            k-=diff   # update k
            if k==0:   # if k is 0 then return
                break
        if k:  # second case  # we have finish nums but wnat to add more numbers
            sum+=(k*(2*prev+k+1)//2)   # use formual 2 of A.P. we take d=1
        return sum