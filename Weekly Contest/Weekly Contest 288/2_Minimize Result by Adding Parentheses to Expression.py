# 2232. Minimize Result by Adding Parentheses to Expression
# https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/

class Solution:
    def minimizeResult(self, expression):

        def evaluate(s):
            return eval(s.replace('(','*(').replace(')',')*').lstrip('*').rstrip('*'))

        ans=[float('inf'),""]
        idx=expression.index('+')
        n=len(expression)
        for left in range(idx):
            for right in range(idx+1,n):
                exp=f'{expression[:left]}({expression[left:idx]}+{expression[idx+1:right+1]}){expression[right+1:n]}'
                temp=evaluate(exp)
                if temp<ans[0]:
                    ans[0]=temp
                    ans[1]=exp
        return ans[1]


        '''
        # Accepted but bad code 
        idx=expression.index('+')
        left=[]
        right=[]
        for i in range(idx):
            first=expression[i:idx]
            if i==0:
                second=0
            else:
                second=expression[0:i]
            left.append([int(first),int(second)])
        for i in range(len(expression)-1,idx,-1):
            first=expression[i:idx:-1]
            if i==len(expression)-1:
                second=0
            else:
                second=expression[i+1:]
            right.append([int(first[::-1]),int(second)])
        ans=float('inf')
        checki=0
        checkj=0
        for i in left:
            for j in right:
                ii=jj=0
                if i[1]==0:
                    checki=1
                    ii=1
                if j[1]==0:
                    checkj=1
                    jj=1
                temp=max(i[1],ii)*(i[0]+j[0])*max(jj,j[1])
                if temp<ans:
                    ans=temp
                    ll=""
                    if not checki:
                        ll+=str(i[1])
                    ll+='(' + str(i[0]) + '+' + str(j[0])+')'
                    if not checkj:
                        ll+=str(j[1])
                    checki=0
                    checkj=0
        return ll
        '''