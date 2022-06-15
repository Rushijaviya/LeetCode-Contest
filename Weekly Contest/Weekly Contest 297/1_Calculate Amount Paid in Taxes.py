# 2303. Calculate Amount Paid in Taxes
# https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution:
    def calculateTax(self, brackets, income):
        '''
        tax=0
        brackets.insert(0,[0,0])
        for i in range(1,len(brackets)):
            if brackets[i][0]-brackets[i-1][0]>=income:
                tax+=(income*(brackets[i][1]/100))
                break
            else:
                income-=(brackets[i][0]-brackets[i-1][0])
                tax+=((brackets[i][0]-brackets[i-1][0])*(brackets[i][1]/100))
        return tax
        '''
        
        tax=prev=0
        for i in range(len(brackets)):
            tax+=(max(0.0,(-prev+min(income,brackets[i][0]))*(brackets[i][1]/100)))
            prev=brackets[i][0]
        return tax