# 2231. Largest Number After Digit Swaps by Parity
# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    def largestInteger(self, num: int) -> int:
        num=[int(i) for i in str(num)]
        odd=[]
        even=[]
        for i in num:
            if i%2:
                odd.append(i)
            else:
                even.append(i)
        odd.sort()
        even.sort()
        ans=[]
        for i in range(len(num)):
            if num[i]%2:
                ans.append(odd.pop())
            else:
                ans.append(even.pop())
        c="".join(str(i) for i in ans)
        return int(c)