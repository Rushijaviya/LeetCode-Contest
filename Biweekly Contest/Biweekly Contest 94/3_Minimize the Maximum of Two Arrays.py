# 2513. Minimize the Maximum of Two Arrays
# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

from math import lcm

class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        '''
        @lru_cache(None)
        def dp(idx,count1,count2):
            if count1==uniqueCnt1 and count2==uniqueCnt2:
                return idx-1
            temp=float('inf')
            if count1<uniqueCnt1:
                if idx%divisor1:
                    temp=min(temp,dp(idx+1,count1+1,count2))
            if count2<uniqueCnt2:
                if idx%divisor2:
                    temp=min(temp,dp(idx+1,count1,count2+1))
            if temp==float('inf'):
                temp=dp(idx+1,count1,count2)
            return temp
            
        return dp(1,0,0)
        '''

        '''
        if divisor1>divisor2:
            return self.minimizeSet(divisor2,divisor1,uniqueCnt2,uniqueCnt1)
        if divisor1%divisor2 and divisor2%divisor1 and (uniqueCnt1+uniqueCnt2)<(divisor1*divisor2) and uniqueCnt1<divisor1 and uniqueCnt2<divisor2:
            return uniqueCnt1+uniqueCnt2
        start=1
        not_used=[]
        count=0
        while count<uniqueCnt1:
            if start%divisor1:
                count+=1
            else:
                not_used.append(start)
            start+=1
        count=0
        for i in not_used:
            if i%divisor2:
                count+=1
        not_used2=[]
        while count<uniqueCnt2:
            if start%divisor2:
                count+=1
            else:
                not_used2.append(start)
            start+=1
        count=0
        for i in not_used2:
            if i%divisor1:
                count+=1
                if count==uniqueCnt1:
                    break
        return start-1-count
        '''

        def valid(total):
            x=total-total//divisor1
            y=total-total//divisor2
            z=total-total//lcm(divisor1,divisor2)
            return x>=uniqueCnt1 and y>=uniqueCnt2 and z>=(uniqueCnt2+uniqueCnt1)

        start=0
        end=10**10
        ans=0
        while start<=end:
            mid=(start+end)//2
            if valid(mid):
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
        
        '''
        start=0
        end=10**10
        while start<=end:
            mid=(start+end)//2
            x,y,z=mid-mid//divisor1,mid-mid//divisor2,mid-mid//lcm(divisor1,divisor2)
            if x>=uniqueCnt1 and y>=uniqueCnt2 and z>=(uniqueCnt1+uniqueCnt2):
                end=mid-1
            else:
                start=mid+1
        return end+1
        '''

        # return bisect_left(range(10**10),True,key=lambda mid:(mid-mid//divisor1)>=uniqueCnt1 and (mid-mid//divisor2)>=uniqueCnt2 and (mid-mid//lcm(divisor1,divisor2))>=(uniqueCnt1+uniqueCnt2))