# 2582. Pass the Pillow
# https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        round=time//(n-1)
        idx=time%(n-1)
        return idx+1 if round%2==0 else n-idx