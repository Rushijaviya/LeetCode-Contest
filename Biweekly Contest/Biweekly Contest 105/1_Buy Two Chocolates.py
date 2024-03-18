# 2706. Buy Two Chocolates
# https://leetcode.com/problems/buy-two-chocolates/

class Solution:
    def buyChoco(self, prices, money):
        '''
        prices.sort()
        if prices[0]+prices[1]>money:
            return money
        return money-prices[0]-prices[1]
        '''

        num1,num2=float('inf'),float('inf')
        for num in prices:
            if num<=num1:
                num2=num1
                num1=num
            elif num<num2:
                num2=num
        return money if money<num1+num2 else money-num1-num2