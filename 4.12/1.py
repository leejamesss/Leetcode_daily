
#暴力匹配

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if len(needle) > len(haystack):
            return -1
        i, j = 0, 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return i - j
                j += 1
            else:
                i -= j
                j = 0
            i += 1
        return -1

      
      
#KMP算法
