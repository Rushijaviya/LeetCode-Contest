# 2672. Number of Adjacent Elements With the Same Color
# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution:
    def colorTheArray(self, n, queries):
        ans=[0]
        color = [0]*n
        color[queries[0][0]]=queries[0][1]
        for idx,col in queries[1:]:
            prev=color[idx-1] if idx>0 else 0
            next=color[idx+1] if idx+1<n else 0
            temp=ans[-1]
            if prev and prev==color[idx]:
                temp-=1
            if next and next==color[idx]:
                temp-=1
            color[idx]=col
            if prev and prev==color[idx]:
                temp+=1
            if next and next==color[idx]:
                temp+=1
            ans.append(temp)
        return ans