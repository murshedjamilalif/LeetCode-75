class Solution:
   def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j=0,0

        res = []
        while i < len(word1) and j < len(word2):
        
              res.append(word1[i])
              res.append(word2[i])
              i+=1
              j+=1
        res.append(word1[i:])
        res.append(word2[i:]) 
        return "".join(res)      
a=Solution()
word1="abc"
word2="pqr"
print(a.mergeAlternately(word1, word2))