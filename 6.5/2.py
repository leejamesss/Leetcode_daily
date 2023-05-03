# https://leetcode.cn/problems/palindrome-partitioning/submissions/
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []

        def backtrack(start, path):
            if start >= len(s):
                res.append(path[:])
                return
            for end in range(start, len(s)):
                if s[start:end+1] == s[start:end+1][::-1]:
                    path.append(s[start:end+1])
                    backtrack(end+1, path)
                    path.pop()

        backtrack(0, [])
        return res
