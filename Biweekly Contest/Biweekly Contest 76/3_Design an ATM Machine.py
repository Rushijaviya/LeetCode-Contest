# 2241. Design an ATM Machine
# https://leetcode.com/problems/design-an-atm-machine/

class ATM:

    def __init__(self):
        self.l=[0]*5
        self.val=[20,50,100,200,500]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.l[i]+=banknotesCount[i]

    def withdraw(self, amount):
        take=[0]*5
        for i in range(4,-1,-1):
            take[i]=min(self.l[i],amount//self.val[i])
            amount-=(take[i]*self.val[i])
        if amount==0:
            for i in range(5):
                self.l[i]-=take[i]
            return take
        return [-1]


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)


'''
class ATM:

    def __init__(self):
        self.l=[0]*5

    def deposit(self, banknotesCount):
        for i in range(len(banknotesCount)):
            self.l[i]+=banknotesCount[i]
        

    def withdraw(self, amount):
        if amount>=500:
            d=self.l.copy()
            if amount>=500:
                t=amount//500
                r=amount%500
                if d[-1]>=t:
                    amount=r
                    d[-1]-=t
                else:
                    amount=amount-(500*d[-1])
                    d[-1]=0
            if amount>=200 and d[-2]>0:
                t=amount//200
                r=amount%200
                if d[-2]>=t:
                    amount=r
                    d[-2]-=t
                else:
                    amount=amount-(200*d[-2])
                    d[-2]=0
            if amount>=100 and d[2]>0:
                t=amount//100
                r=amount%100
                if d[2]>=t:
                    amount=r
                    d[2]-=t
                else:
                    amount=amount-(100*d[2])
                    d[2]=0
            if amount>=50 and d[1]>0:
                t=amount//50
                r=amount%50
                if d[1]>=t:
                    amount=r
                    d[1]-=t
                else:
                    amount=amount-(50*d[1])
                    d[1]=0
            if amount>=20 and d[0]>0:
                t=amount//20
                r=amount%20
                if d[0]>=t:
                    amount=r
                    d[0]-=t
                else:
                    amount=amount-(20*d[0])
                    d[0]=0
            if amount!=0:
                return [-1]
            else:
                ans=[]
                for i in range(0,5):
                    ans.append(self.l[i]-d[i])
                self.l=d
                return ans
            
        elif amount>=200:
            d=self.l.copy()
            if amount>=200 and d[-2]>0:
                t=amount//200
                r=amount%200
                if d[-2]>=t:
                    amount=r
                    d[-2]-=t
                else:
                    amount=amount-(200*d[-2])
                    d[-2]=0
            if amount>=100 and d[2]>0:
                t=amount//100
                r=amount%100
                if d[2]>=t:
                    amount=r
                    d[2]-=t
                else:
                    amount=amount-(100*d[2])
                    d[2]=0
            if amount>=50 and d[1]>0:
                t=amount//50
                r=amount%50
                if d[1]>=t:
                    amount=r
                    d[1]-=t
                else:
                    amount=amount-(50*d[1])
                    d[1]=0
            if amount>=20 and d[0]>0:
                t=amount//20
                r=amount%20
                if d[0]>=t:
                    amount=r
                    d[0]-=t
                else:
                    amount=amount-(20*d[0])
                    d[0]=0
            if amount!=0:
                return [-1]
            else:
                ans=[]
                for i in range(0,5):
                    ans.append(self.l[i]-d[i])
                self.l=d
                return ans
         
        elif amount>=100:
            d=self.l.copy()
            if amount>=100 and d[2]>0:
                t=amount//100
                r=amount%100
                if d[2]>=t:
                    amount=r
                    d[2]-=t
                else:
                    amount=amount-(100*d[2])
                    d[2]=0
            if amount>=50 and d[1]>0:
                t=amount//50
                r=amount%50
                if d[1]>=t:
                    amount=r
                    d[1]-=t
                else:
                    amount=amount-(50*d[1])
                    d[1]=0
            if amount>=20 and d[0]>0:
                t=amount//20
                r=amount%20
                if d[0]>=t:
                    amount=r
                    d[0]-=t
                else:
                    amount=amount-(20*d[0])
                    d[0]=0
            if amount!=0:
                return [-1]
            else:
                ans=[]
                for i in range(0,5):
                    ans.append(self.l[i]-d[i])
                self.l=d
                return ans
            
        elif amount>=50:
            d=self.l.copy()
            if amount>=50 and d[1]>0:
                t=amount//50
                r=amount%50
                if d[1]>=t:
                    amount=r
                    d[1]-=t
                else:
                    amount=amount-(50*d[1])
                    d[1]=0
            if amount>=20 and d[0]>0:
                t=amount//20
                r=amount%20
                if d[0]>=t:
                    amount=r
                    d[0]-=t
                else:
                    amount=amount-(20*d[0])
                    d[0]=0
            if amount!=0:
                return [-1]
            else:
                ans=[]
                for i in range(0,5):
                    ans.append(self.l[i]-d[i])
                self.l=d
                return ans
            
        elif amount>=20:
            d=self.l.copy()
            if amount>=20 and d[0]>0:
                t=amount//20
                r=amount%20
                if d[0]>=t:
                    amount=r
                    d[0]-=t
                else:
                    amount=amount-(20*d[0])
                    d[0]=0
            if amount!=0:
                return [-1]
            else:
                ans=[]
                for i in range(0,5):
                    ans.append(self.l[i]-d[i])
                self.l=d
                return ans
            
        else:
            return [-1]
            

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
'''