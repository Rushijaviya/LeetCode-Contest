# 2280. Minimum Lines to Represent a Line Chart
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution:
    def minimumLines(self, stockPrices):
        n=len(stockPrices)
        if n<=1:
            return 0
        ans=1
        stockPrices.sort()
        for i in range(2,n):
            a=(stockPrices[i][1]-stockPrices[i-1][1])*(stockPrices[i-1][0]-stockPrices[i-2][0])
            b=(stockPrices[i-1][1]-stockPrices[i-2][1])*(stockPrices[i][0]-stockPrices[i-1][0])
            if a!=b:
                ans+=1
        return ans