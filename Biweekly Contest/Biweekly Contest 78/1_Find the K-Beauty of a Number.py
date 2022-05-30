# 2269. Find the K-Beauty of a Number
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num, k):
        count=0
        temp=str(num)
        n=len(temp)
        for i in range(n-k+1):
            try:
                if num%int(temp[i:i+k])==0:
                    count+=1
            except:
                pass
        return count
        
        '''
        s = str(num)
        return sum( int(s[i:i+k]) != 0 and num % int(s[i:i+k]) == 0 for i in range(len(s)-k+1) )
        '''
        
        '''
        pow=1
        cur=ans=0
        temp=num
        while num>0:
            cur+=((num%10)*pow)
            k-=1
            if k>0:
                pow*=10
            else:
                ans+=(cur and not temp%cur)
                cur//=10
            num//=10
        return ans
        '''