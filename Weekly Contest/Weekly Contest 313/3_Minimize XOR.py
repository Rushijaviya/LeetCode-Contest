# 2429. Minimize XOR
# https://leetcode.com/problems/minimize-xor/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        '''
        total_bits=0
        for i in range(32):
            if num2&(1<<i):
                total_bits+=1
        bit=31
        ans=0
        while bit>=0 and total_bits>0:
            if num1&(1<<bit):
                ans|=(1<<bit)
                total_bits-=1
            bit-=1
        bit=0
        while total_bits>0:
            if not ans&(1<<bit):
                ans|=(1<<bit)
                total_bits-=1
            bit+=1
        return ans
        '''

        total_bits=num2.bit_count()
        ans=(1<<total_bits)-1
        idx1=31
        idx2=total_bits-1
        while ans<num1 and idx2>=0:
            while not num1&(1<<idx1):
                idx1-=1
            ans+=((1<<idx1)-(1<<idx2))
            idx1-=1
            idx2-=1
        return ans