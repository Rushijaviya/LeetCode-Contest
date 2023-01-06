# 2397. Maximum Rows Covered by Columns
# https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution:
    def maximumRows(self, matrix, numSelect: int) -> int:
        '''
        def getrow(arr):
            count=0
            for i in range(m):
                for j in coltocover[i]:
                    if  j not in arr:
                        break
                else:
                    count+=1
            return count

        def rec(idx,taken):
            if idx==n or len(taken)==numSelect:
                temp=getrow(taken)
                nonlocal ans
                ans=max(ans,temp)
                return 
            rec(idx+1,taken+[idx])
            rec(idx+1,taken)

        coltocover={}
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            temp=[]
            for j in range(n):
                if matrix[i][j]:
                    temp.append(j)
            coltocover[i]=temp
        
        ans=0
        rec(0,[])
        return ans
        '''
        
        '''
        def getrow(arr):
            count=0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] and j not in arr:
                        break
                else:
                    count+=1
            return count


        ans=0
        m,n=len(matrix),len(matrix[0])
        comb=list(combinations([i for i in range(n)],numSelect))
        for arr in comb:
            ans=max(ans,getrow(arr))
        return ans
        '''

        m,n=len(matrix),len(matrix[0])
        ans=0
        mask=0
        while mask<(1<<n):
            if mask.bit_count()!=numSelect:
                mask+=1
                continue
            count=0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] and ((mask>>j)&1)==0:
                        break
                else:
                    count+=1
            ans=max(ans,count)
            mask+=1
        return ans