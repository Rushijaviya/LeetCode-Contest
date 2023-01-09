# 2406. Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals) -> int:
        '''
        # TLE
        intervals.sort()
        l=[]
        for i,j in intervals:
            if not l:
                l.append([[i,j]])
            else:
                for k in l:
                    for x,y in k:
                        if (x<=i<=y or x<=j<=y or i<=x<=j or i<=y<=j):
                            break
                    else:
                        k.append([i,j])
                        break
                else:
                    l.append([[i,j]])
        return len(l)
        '''
        
        arr=[]
        for i,j in intervals:
            arr.append([i,0])
            arr.append([j,1])
        arr.sort()
        curr=0
        ans=0
        for i,j in arr:
            if j==0:
                curr+=1
                ans=max(ans,curr)
            else:
                curr-=1
        return ans
        
        '''
        arr=[]
        intervals.sort()
        for i,j in intervals:
            if arr and arr[0]<i:
                heappop(arr)
            heappush(arr,j)
        return len(arr)
        '''