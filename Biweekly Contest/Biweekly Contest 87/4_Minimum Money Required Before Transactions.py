# 2412. Minimum Money Required Before Transactions
# https://leetcode.com/problems/minimum-money-required-before-transactions/

class Solution:
    def minimumMoney(self, transactions):
        '''
        arr1,arr2=[],[]
        for cost,cashback in transactions:
            if cashback>=cost:
                arr2.append([cost,cashback])
            else:
                arr1.append([cost,cashback])
        arr1.sort(key=lambda x:x[1])
        arr2.sort(key=lambda x:-x[0])
        transactions=arr1+arr2
        ans=transactions[0][0]
        curr=transactions[0][0]
        for i,j in transactions:
            if curr<i:
                ans+=(i-curr)
                curr=i
            curr-=i
            curr+=j
        return ans
        '''
        
        '''
        s=sum(i-j for i,j in transactions if i>j)
        return max(s+j if i>j else s+i for i,j in transactions)
        '''

        ans=0
        add=0
        for i,j in transactions:
            ans+=max(0,i-j)
            add=max(add,min(i,j))
        return ans+add