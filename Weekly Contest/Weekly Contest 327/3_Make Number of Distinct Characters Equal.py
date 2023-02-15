# 2531. Make Number of Distinct Characters Equal
# https://leetcode.com/problems/make-number-of-distinct-characters-equal/

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        '''
        # TLE
        @lru_cache(None)
        def dp(idx1,idx2):
            if idx1==n or idx2==m:
                return False            
            arr1[ord(word2[idx2])-97]+=1
            arr1[ord(word1[idx1])-97]-=1
            arr2[ord(word2[idx2])-97]-=1
            arr2[ord(word1[idx1])-97]+=1
            if arr1.count(0)==arr2.count(0):
                return True
            arr1[ord(word2[idx2])-97]-=1
            arr1[ord(word1[idx1])-97]+=1
            arr2[ord(word2[idx2])-97]+=1
            arr2[ord(word1[idx1])-97]-=1
            return dp(idx1+1,idx2) or dp(idx1,idx2+1)
            
        arr1,arr2=[0]*26,[0]*26
        for char in word1:
            arr1[ord(char)-97]+=1
        for char in word2:
            arr2[ord(char)-97]+=1
        n,m=len(word1),len(word2)
        return dp(0,0)
        '''

        arr1,arr2=[0]*26,[0]*26
        for char in word1:
            arr1[ord(char)-97]+=1
        for char in word2:
            arr2[ord(char)-97]+=1
        count1,count2=0,0
        for i in range(26):
            count1+=(arr1[i]!=0)
            count2+=(arr2[i]!=0)
        for i in range(26):
            for j in range(26):
                if arr1[i] and arr2[j]:
                    prev1,prev2=count1,count2
                    if arr1[i]==1:
                        count1-=1
                    if arr2[j]==1:
                        count2-=1
                    if arr1[j]==0 or (i==j and arr1[i]==1):
                        count1+=1
                    if arr2[i]==0 or (i==j and arr2[i]==1):
                        count2+=1
                    if count1==count2:
                        return True
                    count1,count2=prev1,prev2
        return False