# 2578. Split With Minimum Sum
# https://leetcode.com/problems/split-with-minimum-sum/

class Solution:
    def splitNum(self, num: int) -> int:
        '''
        nums=list(str(num))
        nums.sort()
        n=len(nums)
        idx=0
        while idx<n and nums[idx]==0:
            idx+=1
        num1,num2="",""
        while idx<n:
            if len(num1)<=len(num2):
                num1+=nums[idx]
            else:
                num2+=nums[idx]
            idx+=1
        if not num1:
            num1=0
        if not num2:
            num2=0
        return int(num1)+int(num2)
        '''
        
        '''
        num="".join(sorted(str(num)))
        return int(num[::2])+int(num[1::2])
        '''

        digit=[]
        while num:
            digit.append(num%10)
            num//=10
        ans=0
        if len(digit)%2:
            digit.append(0)
        digit.sort()
        for i in range(0,len(digit),2):
            ans=ans*10+digit[i]+digit[i+1]
        return ans