# 2595. Number of Even and Odd Bits
# https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution:
    def evenOddBit(self, n):
        '''
        s=bin(n)[2:][::-1]
        even,odd=0,0
        for idx,val in enumerate(s):
            if val=='1':
                even+=(idx%2==0)
                odd+=(idx%2)
        return [even,odd]
        '''
        
        '''
        even,odd=0,0
        for idx in range(11):
            if n&(1<<idx):
                even+=(idx%2==0)
                odd+=(idx%2)
        return [even,odd]
        '''

        return [(n&(0b0101010101)).bit_count(),(n&(0b01010101010)).bit_count()]