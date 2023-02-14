# 2525. Categorize Box According to Criteria
# https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky,heavy=False,False
        if max(length,width,height,mass)>=10000 or (length*width*height)>=10**9:
            bulky=True
        if mass>=100:
            heavy=True
        if bulky and heavy:
            return "Both"
        if bulky:
            return "Bulky"
        if heavy:
            return "Heavy"
        return "Neither"

        # return ("Neither", "Bulky", "Heavy", "Both")[int(length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 10**9) + 2*(mass >= 100)]