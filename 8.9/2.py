class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n=len(secret)
        import collections
        hash_map=collections.defaultdict(int)
        bulls=cows=0
        for i in range(n):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                hash_map[secret[i]]+=1
        for i in range(n):
            if secret[i]!=guess[i] and hash_map[guess[i]]>0:
                cows+=1
                hash_map[guess[i]] -=1
        return str(bulls)+'A'+str(cows)+'B'
# https://leetcode.cn/problems/bulls-and-cows/submissions/
