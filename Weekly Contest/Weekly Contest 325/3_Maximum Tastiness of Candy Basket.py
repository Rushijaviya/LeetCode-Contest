# 2517. Maximum Tastiness of Candy Basket
# https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

class Solution:
    def maximumTastiness(self, price, k):

        def valid(target):
            prev=price[0]
            count=1
            for num in price[1:]:
                if num-prev>=target:
                    prev=num
                    count+=1
            return count>=k

        price.sort()
        start=0
        end=price[-1]-price[0]
        while start<=end:
            mid=(start+end)//2
            if valid(mid):
                start=mid+1
            else:
                end=mid-1
        return start-1