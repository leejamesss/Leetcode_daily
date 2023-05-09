# https://leetcode.cn/problems/compare-version-numbers/submissions/
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
      
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        n1, n2 = len(v1), len(v2)
        if n1 < n2:
            v1 += [0] * (n2 - n1)
        if n2 < n1:
            v2 += [0] * (n1 - n2)
        for i in range(max(n1, n2)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0
