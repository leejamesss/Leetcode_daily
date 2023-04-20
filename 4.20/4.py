#https://leetcode.cn/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst=s.rstrip().lstrip().split()
        return len(lst[-1])
