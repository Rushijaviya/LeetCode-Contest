# 2515. Shortest Distance to Target String in a Circular Array
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution:
    def closetTarget(self, words, target, startIndex):
        '''
        if target not in words:
            return -1
        if words[startIndex]==target:
            return 0
        for left in range(startIndex-1,-1,-1):
            if words[left]==target:
                ans=startIndex-left
                break
        else:
            left=len(words)-1
            while left>=0:
                if words[left]==target:
                    break
                left-=1
            ans=startIndex+(len(words)-left)
        for right in range(startIndex+1,len(words)):
            if words[right]==target:
                ans=min(ans,right-startIndex)
                break
        else:
            right=0
            while right<len(words):
                if words[right]==target:
                    break
                right+=1
            ans=min(ans,len(words)-startIndex+right)
        return ans
        '''
        
        '''
        index=[]
        for idx,word in enumerate(words):
            if word==target:
                if idx==startIndex:
                    return 0
                index.append(idx)
        if not index:
            return -1
        ans=float('inf')
        for idx in index:
            if idx<startIndex:
                temp=min(startIndex-idx,len(words)-startIndex+idx)
            else:
                temp=min(idx-startIndex,startIndex+len(words)-idx)
            ans=min(ans,temp)
        return ans
        '''

        ans=float('inf')
        for idx,word in enumerate(words):
            if word==target:
                ans=min(ans,abs(startIndex-idx),len(words)-abs(startIndex-idx))
        return ans if ans!=float('inf') else -1