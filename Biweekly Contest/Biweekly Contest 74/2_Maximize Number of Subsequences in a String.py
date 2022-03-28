# 2207. Maximize Number of Subsequences in a String
# https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

class Solution:
    def maximumSubsequenceCount(self, text, pattern):
        ans=count1=count2=0
        for i in text:
            if i==pattern[1]:
                ans+=count1
                count2+=1
            if i==pattern[0]:
                count1+=1
        return ans+max(count1,count2)