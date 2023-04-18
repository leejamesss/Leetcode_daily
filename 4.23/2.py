# https://leetcode.cn/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            arr = list(s)
            arr.sort()
            sorted_str = ''.join(arr)
            if sorted_str not in d:
                d[sorted_str] = [s]
            else:
                d[sorted_str].append(s)
        return list(d.values())
#哈希表
