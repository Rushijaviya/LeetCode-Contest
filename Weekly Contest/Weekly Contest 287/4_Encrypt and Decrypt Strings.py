# 2227. Encrypt and Decrypt Strings
# https://leetcode.com/problems/encrypt-and-decrypt-strings/

class Encrypter:
    
    def __init__(self, keys, values, dictionary):
        self.enc={}
        self.count={}
        for i in range(len(keys)):
            self.enc[keys[i]]=values[i]
        for i in dictionary:
            x=self.encrypt(i)
            self.count[x]=self.count.get(x,0)+1
            

    def encrypt(self, word1: str) -> str:
        res=""
        for i in word1:
            res+=self.enc.get(i,'0')
        return res

    def decrypt(self, word2: str) -> int:
        return self.count.get(word2,0)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)