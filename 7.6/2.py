class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapping_st, mapping_ts = {}, {}
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if char_s in mapping_st and mapping_st[char_s] != char_t:
                return False
            if char_t in mapping_ts and mapping_ts[char_t] != char_s:
                return False
            mapping_st[char_s], mapping_ts[char_t] = char_t, char_s
        return True
      
#       https://leetcode.cn/problems/isomorphic-strings/submissions/
