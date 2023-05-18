
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        mp = {}
        for i in range(n):
            mask = 0
            for c in words[i]:
                mask |= 1 << (ord(c) - ord('a'))
            mp[mask] = max(mp.get(mask, 0), len(words[i]))

        ans = 0
        for x in mp:
            for y in mp:
                if x & y == 0:
                    ans = max(ans, mp[x] * mp[y])

        return ans
#       https://leetcode.cn/problems/maximum-product-of-word-lengths/submissions/
