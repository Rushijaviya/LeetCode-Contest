# 2299. Strong Password Checker II
# https://leetcode.com/problems/strong-password-checker-ii/

import re

class Solution:
    def strongPasswordCheckerII(self, password):
        '''
        return re.match(r'^(?!.*([0-9])\1)(?!.*([a-z])\2)(?!.*([A-Z])\3)(?!.*([!@#$%^&*()+-])\4)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()+-])[A-Za-z0-9!@#$%^&*()+-]{8,}$', password)
        '''
        if len(password)<8:
            return False
        lower=digit=upper=special=False
        if password[0].islower():
            lower=True
        elif password[0].isupper():
            upper=True
        elif password[0].isdigit():
            digit=True
        else:
            special=True
        for i in range(1,len(password)):
            if password[i]==password[i-1]:
                return False
            if password[i].islower():
                lower=True
            elif password[i].isupper():
                upper=True
            elif password[i].isdigit():
                digit=True
            else:
                special=True
        if lower and digit and upper and special:
            return True
        return False