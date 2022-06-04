# 2288. Apply Discount to Prices
# https://leetcode.com/problems/apply-discount-to-prices/

class Solution:
    def discountPrices(self, sentence, discount):
        '''
        idx=0
        n=len(sentence)
        dis=discount/100
        ans=""
        while idx<n:
            if sentence[idx]=='$':
                ans+='$'
                j=idx+1
                word=""
                if idx-1<0 or sentence[idx-1]==' ':
                    while j<n and ord(sentence[j]) in range(48,58):
                        word+=sentence[j]
                        j+=1
                    if len(word) and (j>=n or sentence[j]==' ') :
                        ans+="{:.2f}".format(int(word)-int(word)*dis)
                    else:
                        ans+=sentence[idx+1:j]
                idx=j
            else:
                ans+=sentence[idx]
                idx+=1
        return ans
        '''

        
        l=list(map(str,sentence.split()))
        ans=""
        dis=discount/100
        for word in l:
            if word[0]=='$' and word[1:].isnumeric():
                ans+='$'
                ans+="{:.2f}".format(int(word[1:])-int(word[1:])*dis)
                ans+=" "
            else:
                ans+=word
                ans+=" "
        return ans[:-1]
        
        '''
        return " ".join(f"${(int(word[1:])*(1-(discount/100))):.2f}" if word[0]=='$' and word[1:].isnumeric() else word for word in sentence.split())
        '''