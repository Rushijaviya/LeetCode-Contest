# 2201. Count Artifacts That Can Be Extracted
# https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

class Solution:
    def digArtifacts(self, n, artifacts, dig):
        dig=set((r,c) for r,c in dig)
        ans=0
        for i in artifacts:
            c=1
            for j in range(i[0],i[2]+1):
                for k in range(i[1],i[3]+1):
                    if (j,k) not in dig:
                        c=0
            if c:
                ans+=1
        return ans